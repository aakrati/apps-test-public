from fastapi import FastAPI
import gradio as gr

app = FastAPI()

def greet(name):
    return "Hola , " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

app = gr.mount_gradio_app(app, demo, path="/")