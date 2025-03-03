import gradio as gr
import requests

# FastAPI backend URL
BASE_URL = "http://127.0.0.1:8000"

# Store JWT token after login
jwt_token = None

def login(username, password):
    global jwt_token
    response = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password}).json()

    if "token" in response:
        jwt_token = response["token"]
        return f"Welcome, {username}!", gr.update(visible=True)
    
    return "Invalid username or password.", gr.update(visible=False)

def chatbot_response(user_input, history=[]):
    global jwt_token
    if not jwt_token:
        return "Please log in first."

    headers = {"Authorization": f"Bearer {jwt_token}"}
    response = requests.post(f"{BASE_URL}/chat", json={"user_input": user_input}, headers=headers).json()
    
    return response.get("response", "Something went wrong.")

def logout():
    global jwt_token
    jwt_token = None
    return "You have been logged out. Please log in again.", gr.update(visible=False)

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# Warehouse Management Chatbot")

    with gr.Row():
        gr.Markdown("### Please Log In")
        login_box = gr.Textbox(label="Username")
        password_box = gr.Textbox(label="Password", type="password")
        login_button = gr.Button("Login")
        login_status = gr.Markdown(visible=False)

    with gr.Row(visible=False) as chat_ui:
        gr.Markdown("### Chat with the AI")
        chat = gr.ChatInterface(fn=chatbot_response)
        logout_button = gr.Button("Logout")

    login_button.click(login, inputs=[login_box, password_box], outputs=[login_status, chat_ui])
    logout_button.click(logout, outputs=[login_status, chat_ui])

demo.launch()
