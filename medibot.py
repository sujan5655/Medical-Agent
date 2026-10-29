import streamlit as st
import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains import RetrievalQA

from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langchain_openai import ChatOpenAI


from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()



DB_FAISS_PATH="vectorstore/db_faiss"
@st.cache_resource
def get_vectorstore():
    embedding_model=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    db=FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
    return db


def set_custom_prompt(custom_prompt_template):
    prompt=PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])
    return prompt


def load_llm():
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. "
            "Please add it to your .env file."
        )

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=api_key,
        temperature=0.3,
        max_tokens=512,
    )

    return llm


def main():
  st.title("Ask Chatbot")
  if 'messages' not in st.session_state:
    st.session_state.messages=[]
  for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])
  prompt=st.chat_input("Pass your prompt here")
  if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({'role':'user','content':prompt})
    # response="Hi, I am Medibot"


    
    CUSTOM_PROMPT_TEMPLATE = """
           If you dont know the answer, just say that you            dont know, dont try to make up an answer. 
           Use the pieces of information provided in the            context to answer user's question.
           Dont provide anything out of the given context

           Context: {context}
           Question: {question}

           Start the answer directly. No small talk please.
           """
    llm=load_llm()

    try:
       vectorstore=get_vectorstore()
       if vectorstore is None:
          st.error("Failed to load the vector store")
       # Create the QA chain
       qa_chain = RetrievalQA.from_chain_type(
            llm=load_llm(),
            chain_type="stuff",
            retriever=vectorstore.as_retriever(
               search_kwargs={"k": 3}
               ),
            return_source_documents=True,
              chain_type_kwargs={
        "prompt": set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)
    },
        )
       response=qa_chain.invoke({'query': prompt})
       result=response["result"]
       source_documents=response["source_documents"]
       result_to_show=result+"\nSource Docs:\n"+str(source_documents)



       st.chat_message('assistant').markdown(result_to_show)
       st.session_state.messages.append({'role':'assistant','content':result_to_show})

    except Exception as e:
       st.error(f"Error: {str(e)}")

if __name__=="__main__":
  main()