import chainlit as cl
import openai
import os

os.environ['OPENAI_API_KEY'] = ''
openai.api_key = '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'
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


    await cl.Message(content = f"{response['choices'][0]['message']['content']}",).send()