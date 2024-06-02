# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 09:18:09 2023

@author: Windows
"""


from langchain.agents import load_tools
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
import streamlit as st
import os

# Load API keys from environment variables for enhanced security
openai_api_key = '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'
serpapi_api_key = '52d8b4fce32da10d2f8e25a885d2684acec0f7f49627cbc0c8aed887cfe7d5f3'

if not openai_api_key or not serpapi_api_key:
    raise ValueError("API keys for OpenAI or SerpAPI are not set in environment variables.")

# Initialize the OpenAI instance with the API key loaded from environment variables
llm = OpenAI(temperature=0, api_key=openai_api_key)

def generate_response(query):
    """
    Generates a response using the Langchain agent based on the provided query.
    This function uses the OpenAI and SerpAPI tools to process the query.
    """
    try:
        tool_names = ["serpapi"]
        tools = load_tools(tool_names)
        
        agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=False)
        
        response = agent.run(query)
        return response
    except Exception as e:
        return f"An error occurred: {e}"

#----------------STREAMLIT APP------------------
st.title("AMMP AI and Energy Data Engineer Internship Technical Assessment")
st.subheader('Third Case Study')
st.write('In this case study, I used only the SERPAPI API together with the OpenAI API for generating responses to users. This basically searches the internet for responses.')
st.sidebar.text('Developed by Samuel Shaibu')

# User input for prompt
user_prompt = st.text_input("Enter your prompt:")

if user_prompt:
    # Generate response and display it
    response = generate_response(user_prompt)
    st.write(response)
