from langchain.embeddings.openai import OpenAIEmbeddings
import os
import pinecone 
from langchain.vectorstores import Pinecone
from text_preprocess import TextProcessor
from gmail_fetch import GmailAPI
from langchain.chat_models import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain import OpenAI
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
load_dotenv('.env')

text_processor = TextProcessor()
gmail_api = GmailAPI()
email_data_list = gmail_api.get_emails(2)
    
data = []
for email_data in email_data_list:
    # print(email_data)
    processed_email_data = text_processor.preprocess_email_data(email_data)
    data.append(processed_email_data)


      
# print (data)
print(len(data))
data = [
    str(email) for email in data
]
print(len(data))
# print(data)

openai_api_key = os.getenv('OPENAI_API_KEY')

model_name = 'text-embedding-ada-002'

embeddings = OpenAIEmbeddings(
    model=model_name,
    openai_api_key=openai_api_key
)

vectorstore = FAISS.from_texts(texts=data, embedding=embeddings)  
print(vectorstore)  
llm = ChatOpenAI()
memory = ConversationBufferMemory(
            memory_key='chat_history', return_messages=True)
conversation_chain = ConversationalRetrievalChain.from_llm(
            llm= ChatOpenAI(model_kwargs={'api_key': openai_api_key}),
            retriever=vectorstore.as_retriever(),
            memory=memory
          )

def conversation():
    while True:
        user_input = input(">>> ")
        if user_input == "quit":
            break
        else:
            print(conversation_chain.run(user_input))

conversation()