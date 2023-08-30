from langchain.text_splitter import CharacterTextSplitter
from gmail_fetch import GmailAPI
import re

class TextProcessor:
    def __init__(self):
        self.url_pattern = re.compile(r'https?://\S+|www\.\S+')
        self.text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

    def remove_html_tags(self, text):
        """Removes all HTML tags from the text"""
        return re.sub(r'<[^>]+>', '', text)

    def remove_links(self, text):
        """Replaces URLs with an empty string"""
        text_without_links = self.url_pattern.sub('', text)
        return text_without_links

    def preprocess_email_data(self, email_data):
        preprocessed_body = self.remove_html_tags(email_data['Body'])
        processed_email_data = {
            'From': email_data['From'],
            'Date': email_data['Date'],
            'Subject': email_data['Subject'],
            'Body': preprocessed_body,
            'Labels': email_data['Labels']
        }
        return processed_email_data

    def get_text_chunks_from_email_data(self, processed_email_data):
        text_chunks = self.text_splitter.split_text(processed_email_data['Body'])
        return text_chunks

    # text_processor = TextProcessor()
    # gmail_api = GmailAPI()
    # email_data_list = gmail_api.get_emails(2)
    

    # for email_data in email_data_list:
    #     processed_email_data = text_processor.preprocess_email_data(email_data)
    #     text_chunks = text_processor.get_text_chunks_from_email_data(processed_email_data)
        
    #     for chunk in text_chunks:
    #         print(chunk)
