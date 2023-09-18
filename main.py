import chainlit as cl
import openai
import os

os.environ['OPENAI_API_KEY'] = ''

#return everything that the user inputs.

@cl.on_message
async def main(message: str):
    await cl.Message(content = message).send()