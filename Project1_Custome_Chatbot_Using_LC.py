import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



# set up the api key for both gemini api key  and langsmith api key
os.environ["Google_Api_Key"]='AQ.Ab8RN6LKHgIlTAG-CWAsRfmaUzpfLJU72b4pBBuT7fsNIBLKjA'
os.environ["Langsmith_Trakcing_V2"]='true'
os.environ["Langsmith+Api_Key"]='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'

# Prompt Template

prompt=ChatPromptTemplate.from_messages(
    
    [("system","You are a chatbot which assistant to the world about the latest news."),
     ("human","{question}")
    ]
)

st.title('Gemini chat model with langchain created by Ms.Prerana Sangar')
input_text=st.text_input('How may i helpyou ? if you write one word then I am Hallucinate')

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1, max_output_tokens=1000)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
if input_text:
    with st.spinner('Generating response...'):
        try:
            response = chain.invoke({"question": input_text})
            st.success('Response generated successfully!')
            st.write(response)
        except Exception as e:
            st.error(f'An error occurred: {e}')
