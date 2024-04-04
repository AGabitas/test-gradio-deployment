from fastapi import FastAPI
import gradio as gr

app = FastAPI()

def authenticate_user(username, password):
    if username == 'user' and password == 'pass':
        return True
    return False


io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")

app = gr.mount_gradio_app(app, io, "/", auth=authenticate_user)