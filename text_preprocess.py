from langchain.text_splitter import CharacterTextSplitter  # Make sure to import the necessary module
from gmail_fetch import get_emails
import re 



def get_text_chunks_from_email_data(email_data):
    
    preprocessed_body = email_data['Body']  # Use the preprocessed body from email data
    text_splitter = CharacterTextSplitter(
         separator="\n",
         chunk_size=1000,
         chunk_overlap=200,
         length_function=len
    )
    text_chunks = text_splitter.split_text(preprocessed_body)
    return text_chunks


email_data_list = get_emails(2)

for email_data in email_data_list:
    text_chunks = get_text_chunks_from_email_data(email_data)
    
    print(text_chunks)
