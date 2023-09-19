import chainlit as cl
import openai
import os
from langchain import PromptTemplate, OpenAI, LLMChain

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = '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'

template = """Question: {question}
Answer: Let's think step by step."""

@cl.on_chat_start
def main():
    prompt = PromptTemplate(template = template, input_variables = ["question"])
    llm_chain = LLMChain(
        prompt= prompt,
        llm = OpenAI(temperature= 1, streaming=True),
        verbose = True,
    )
    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message : str):
    llm_chain = cl.user_session.get('llm_chain')
    res = await llm_chain.acall(message, callbacks = [cl.AsyncLangchainCallbackHandler()])
    await cl.Message(content= res["text"]).send()