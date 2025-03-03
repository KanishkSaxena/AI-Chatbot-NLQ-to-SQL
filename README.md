# AI-Powered Warehouse Management Chatbot

## Overview
The **AI-Powered Warehouse Management Chatbot** allows users to efficiently manage warehouse inventory using natural language queries. The system is built using **FastAPI** for the backend, **MongoDB** for data storage, and an **AI processor** to handle natural language queries (NLQ) and map them to database operations.

## Setup
1. create venv

```
python3.10 -m venv ai-chatbot
```

2. Install the required dependencies
```
pip install -r requirements.txt
```
3. 
Setup mongodb
```
brew install mongodb-community@6.0
```

4. Start the Service
```
brew services start mongodb-community@6.0
```
5. Copy the Hugging Face API Key from env_template into enviornment
```
cp env_template.txt .env
```
6. Run the backend
```
uvicorn main:app --reload
```
7. Run the frontend
```
python chat_ui.py
```
## Architecture
The chatbot follows a structured architecture:

1. **AI Application**: Frontend interface for user interaction.
2. **JWT Authentication**: Ensures each user can only access their own data.
3. **FastAPI Backend**: Handles user queries, processes requests, and interacts with MongoDB.
4. **AI Processor (NLQ to MongoDB)**: Converts natural language queries into structured MongoDB queries.
5. **MongoDB**: Stores sectors, warehouses, and inventory logs.

## MongoDB Collections & Schema
The system uses three main collections: **sectors**, **warehouses**, and **logdatas (or logs)**.

### 1. `sectors` Collection
Stores sector details owned by a user.

#### Example Document:
```json
{
    "_id": ObjectId("65d123456789abcd000a101"),
    "name": "Sector 1",
    "creator": ObjectId("65cb123456789abcd000a001"),
    "description": "Main storage sector"
}
```

### 2. `warehouses` Collection
Stores warehouse details and predefined inventory structure.

#### Example Document:
```json
{
    "_id": ObjectId("65cbc1a123456789abcd1001"),
    "name": "Warehouse 1",
    "creator": ObjectId("65cb123456789abcd000a001"),
    "sector": ObjectId("65d123456789abcd000a101"),
    "columns": [
        { "title": "Electronics", "dataIndex": "0" },
        { "title": "Furniture", "dataIndex": "1" }
    ]
}
```

### 3. `logdatas` (or `logs`) Collection
Stores inventory logs for warehouse transactions.

#### Example Document:
```json
{
    "_id": ObjectId("65dee1b123456789abcd2001"),
    "warehouse": ObjectId("65cbc1a123456789abcd1001"),
    "creator": ObjectId("65cb123456789abcd000a001"),
    "logData": {
        "day": "2025-02-14T12:20:36.785Z",
        "0": 250,
        "1": 40
    }
}
```

## Key Functionalities
### 1. **Sector Management**
- Users can retrieve a list of all sectors they have created.

### 2. **Warehouse Management**
- Users can retrieve warehouse details and predefined inventory columns.

### 3. **Logging New Inventory Data**
- The chatbot dynamically prompts the user to enter inventory values based on the warehouse's predefined structure.
- The system automatically maps input values and stores the log entry with a timestamp.

#### Example Conversation:
```
User: "Add a new log in Warehouse 1 in Sector 1."
Chatbot: "Please provide inventory count for Electronics."
User: "250"
Chatbot: "Thanks, now please provide inventory count for Furniture."
User: "40"
Chatbot: "Thanks, your log has been added successfully."
```

## How to Query MongoDB
To retrieve all **sectors** for a particular user:
```python
db.sectors.find({"creator": ObjectId(user_id)})
```
To retrieve all **warehouses** for a user:
```python
db.warehouses.find({"creator": ObjectId(user_id)})
```
To retrieve **log entries** for a specific warehouse:
```python
db.logdatas.find({"warehouse": ObjectId(warehouse_id), "creator": ObjectId(user_id)})
```

## Conclusion
This AI-powered warehouse chatbot simplifies **inventory tracking** and **management** using natural language queries. It ensures **data security** by allowing users to access only their own records through JWT authentication. The chatbot dynamically **prompts users** for required information and logs transactions efficiently in MongoDB.

