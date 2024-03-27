from fastapi import FastAPI
import gradio as gr

app = FastAPI()

with gr.Blocks() as demo:
    gr.Markdown("Hello World")

app = gr.mount_gradio_app(app, demo, path="/")