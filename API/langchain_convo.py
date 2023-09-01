

import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from text_preprocess import TextProcessor
from gmail_fetch import GmailAPI
from langchain.chat_models import ChatOpenAI

# Load environment variables
load_dotenv('.env')

def preprocess_emails():
    text_processor = TextProcessor()
    gmail_api = GmailAPI()
    email_data_list = gmail_api.get_emails(1)
    email_content_list = [(email['From'], email['Date'], email['Subject'], email['Body']) for email in email_data_list]
    processed_data = []

    for email_data in email_content_list:
        processed_email_data = text_processor.preprocess_email_data(email_data)
        processed_data.append(str(processed_email_data))

    return processed_data

def initialize_embeddings_and_vectorstore(data):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    model_name = 'text-embedding-ada-002'

    embeddings = OpenAIEmbeddings(
        model=model_name,
        openai_api_key=openai_api_key
    )

    vectorstore = FAISS.from_texts(texts=data, embedding=embeddings)
    return vectorstore

def initialize_conversation_chain(vectorstore):
    llm = ChatOpenAI(model_kwargs={'api_key': os.getenv('OPENAI_API_KEY')})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain

# data = preprocess_emails()
# print(data)
# print(len(data))
# print(type(data))
# # vectorstore = initialize_embeddings_and_vectorstore(data)
# # conversation_chain = initialize_conversation_chain(vectorstore)

# # while True:
# #     user_input = input(">>> ")
# #     if user_input == "quit":
# #         break
# #     else:
# #         print(conversation_chain.run(user_input))
