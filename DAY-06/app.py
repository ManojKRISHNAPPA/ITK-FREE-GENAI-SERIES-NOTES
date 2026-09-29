import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



st.title("ITK OLLMA CHATBOT")

input_question = st.text_input("Enter your question:")
with st.sidebar:
    st.header("LLM configuration")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.5, 0.1)
    max_tokens = st.slider("Max Tokens", 50, 1000, 200, 50)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are helpfull assitant."),
        ("user","Question: {question} ")
    ]
)

llm = ChatOllama(
    model = "llama3.1:latest",
    temperature = temperature,
)

output_parser = StrOutputParser()


chain =  prompt | llm | output_parser

if input_question:
    response = chain.invoke({"question": input_question})
    st.write(response)

