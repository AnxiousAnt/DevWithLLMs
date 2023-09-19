import chainlit as cl
import openai
import os

os.environ['OPENAI_API_KEY'] = ''
openai.api_key = ''
#return everything that the user inputs.

@cl.on_message
async def main(message: str):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "assistant","content":"you are a helpful assistant"},
            {"role": "user", "content": message}
        ],
        temperature = 1,
    )


    await cl.Message(content = str(response)).send()