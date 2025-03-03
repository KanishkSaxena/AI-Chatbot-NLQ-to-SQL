import json, re,os
import datetime
from dotenv import load_dotenv

load_dotenv()

HF_API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
HF_API_KEY= os.getenv('HUGGING_FACE_API_KEY')
HF_HEADERS = {"Authorization": "Bearer {HF_API_KEY}}"}

import requests
from fastapi import APIRouter, Depends, Request
from motor.motor_asyncio import AsyncIOMotorDatabase
from pydantic import BaseModel
from database import get_database
from bson import ObjectId
from auth import get_current_user

router = APIRouter()

active_log_sessions = {}

# Request model
class ChatRequest(BaseModel):
    user_input: str

# Function to call AI and extract structured intent
def query_huggingface(prompt: str):
    """Calls the AI model and extracts structured responses."""
    response = requests.post(HF_API_URL, headers=HF_HEADERS, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    return "I didn't understand that."

# Chatbot API to process user query
@router.post("/chat")
async def chat_process(
    request: Request, 
    chat_data: ChatRequest, 
    db: AsyncIOMotorDatabase = Depends(get_database),
    user_id: str = Depends(get_current_user)
):
    """Processes user input and retrieves data accordingly."""

    user_input = chat_data.user_input
    print(f"User ID: {user_id}") 

    if user_id in active_log_sessions:
        log_session = active_log_sessions[user_id]
        warehouse_id = log_session["warehouse_id"]
        pending_columns = log_session["pending_columns"]
        collected_data = log_session["collected_data"]

        if pending_columns:
            column = pending_columns.pop(0)
            collected_data[column["dataIndex"]] = user_input
            
            if pending_columns:
                next_column = pending_columns[0]["title"]
                return {"response": f"Thanks! Now provide inventory count for {next_column}."}

            log_entry = {
                "warehouse": ObjectId(warehouse_id),
                "creator": ObjectId(user_id),
                "logData": {
                    "day": datetime.datetime.utcnow().isoformat(),
                    **collected_data
                }
            }
            await db.logdatas.insert_one(log_entry)
            del active_log_sessions[user_id]
            return {"response": "Thanks! Your log has been added successfully."}

    ai_prompt = f""" You are an excellent Inventory Manager assistant and follow the ###Instructions. You excel at understanding requests and provides the answer. You will be given a |<input>| from a user and you ONLY need to return the |<output>|. Input will be a query and it could be classified into four different categories: ["sector_list", "sector_location", "warehouse_info", "log_inventory"] 
    
    1. sector_list ex. Show me my sectors or Tell me my sectors
    2. sector_location ex. Where is Sector 1 located
    3. warehouse_info ex. Show me my warehouses in Sector 2 
    4. log_inventory ex. Add a new log in Warehouse 1 in Sector 1.
    
    
    ###Instructions: 
    
    *Do NOT repeat the prompt or provide explanations.
    *Strictly return a JSON response with no extra text.
    
    User input: "{user_input}"
    
    Your aim is to Determine the intent of the user and select one from the category list: ["sector_info", "sector_location", "warehouse_info", "log_inventory"].
    
    ["sector_list", "sector_location", "warehouse_info", "log_inventory"]

    - If the query is about **listing all sectors**, return:
    {{"intent": "sector_list"}}

    - If the query is about **a specific sector's location**, return:
    {{"intent": "sector_location", "sector": "Sector 1"}}

    - If the query is about **warehouses in a sector**, return:
    {{"intent": "warehouse_info", "sector": "Sector 1"}}

    - If the query is about **logging inventory in a warehouse**, return:
    {{"intent": "log_inventory", "warehouse": "Warehouse 1"}}

    Return only a valid JSON object. No explanations, no extra text.
    
    AI-Response
    """

    ai_data = query_huggingface(ai_prompt)
    print(ai_data)
    pattern = r'AI-Response\s*-+\s*\n\s*(\{"intent":.*?\})'
    match = re.search(pattern, ai_data, re.DOTALL)
    if match:
        ai_response = match.group(1).strip()
        print(f"AI Response: {ai_response}") 

    if '"intent": "sector_list"' in ai_response:
        sectors = await db.sectors.find({"creator": ObjectId(user_id), "deleted": False}).to_list(100)
        if not sectors:
            return {"response": "You have no sectors in your warehouse."}

        return {"response": "Your available sectors: " + ", ".join([s['name'] for s in sectors])}

    elif '"intent": "sector_location"' in ai_response:
        sector_name = ai_response.split('"sector": "')[-1].split('"')[0].strip()
        print(f"Extracted Sector Name: {sector_name}")
        
        sector = await db.sectors.find_one({"name": sector_name, "creator": ObjectId(user_id)})
        if not sector:
            return {"response": f"Sector '{sector_name}' not found."}

        return {"response": f"{sector_name} is located at {sector['location']}."}

    elif '"intent": "warehouse_info"' in ai_response:
        sector_name = ai_response.split('"sector": "')[-1].split('"')[0].strip()
        sector = await db.sectors.find_one({"name": sector_name, "creator": ObjectId(user_id)})

        if not sector:
            return {"response": f"Sector '{sector_name}' not found."}

        warehouses = await db.warehouses.find({"sector": sector["_id"], "creator": ObjectId(user_id)}).to_list(100)
        if not warehouses:
            return {"response": f"No warehouses found in {sector_name}."}

        return {"response": f"Warehouses in {sector_name}: " + ", ".join([w['name'] for w in warehouses])}

    elif '"intent": "log_inventory"' in ai_response:
        warehouse_name = ai_response.split('"warehouse": "')[-1].split('"')[0].strip()
        warehouse = await db.warehouses.find_one({"name": warehouse_name, "creator": ObjectId(user_id)})

        if not warehouse:
            return {"response": f"Warehouse '{warehouse_name}' not found."}

        questions = [{"title": col["title"], "dataIndex": col["dataIndex"]} for col in warehouse.get("columns", []) if col["dataIndex"] != "day"]

        active_log_sessions[user_id] = {
            "warehouse_id": warehouse["_id"],
            "pending_columns": questions,
            "collected_data": {}
        }

        return {"response": f"Let's log inventory for {warehouse_name}. Provide counts for: {questions[0]['title']}."}

