import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


st.set_page_config(page_title="Groq LLM", page_icon="🥃")

st.title("ITK Groq LLM")

# sidebar

with st.sidebar:
    st.header("Groq LLM configuration")

    groq_api_key = st.text_input("Enter yourGroq API Key", type="password",placeholder="gsk_..........")    

    model = st.selectbox("Select a model", ["openai/gpt-oss-120b", "qwen/qwen3.6-27b"])

    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)

    max_tokens = st.slider("Max Tokens", min_value=100, max_value=1000, value=500, step=100)

# User question
question = st.text_input("Enter your question", placeholder="What is the capital of France?")

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can answer questions and help with tasks."),
    ("user", "Question: {question}")
])

if groq_api_key:
    llm = ChatGroq(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=groq_api_key
    )

    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser

    if st.button("Generate"):
        response = chain.invoke({"question": question})
        st.write(response)
else:
    st.error("Please enter your Groq API Key")