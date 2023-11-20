import transformers
import gradio as gr
from transformers import pipeline
import os 
TOKEN = os.getenv('HUGGING_FACE_HUB_TOKEN')

models = [
    "barghavani/English_to_French",
    "barghavani/English_to_German",
    "barghavani/English_to_Hindi",
    #"Helsinki-NLP/opus-mt-ber-fr",
    #"Helsinki-NLP/opus-mt-es-ber",
    #"Helsinki-NLP/opus-mt-ber-es",
    #"Helsinki-NLP/opus-mt-kab-en"
]

pipes = {}

def predict(text, model):
    if model not in pipes:
        pipes[model] = pipeline("translation", model=model)
    pipe = pipes[model]
    return pipe(text)[0]['translation_text']

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Textbox(lines=5, label="Input Text"),
        gr.Dropdown(models, label="Model")
    ],
    outputs='text',
)
demo.launch(share=True,debug=True)