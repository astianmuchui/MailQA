from langchain.text_splitter import CharacterTextSplitter
from gmail_fetch import GmailAPI
import re
from bs4 import BeautifulSoup

class TextProcessor:
    def __init__(self):
        self.url_pattern = re.compile(r'https?://\S+|www\.\S+')

    def remove_html_tags(self, text):
        """Removes all HTML tags from the text"""
        soup = BeautifulSoup(text, 'html.parser')
        return soup.get_text()

    def remove_links(self, text):
        """Replaces URLs with an empty string"""
        text_without_links = self.url_pattern.sub('', text)
        return text_without_links


    def preprocess_email_data(self, email_data):
        preprocessed_body = self.remove_html_tags(email_data[3])
        preprocessed_body = self.remove_links(preprocessed_body)
        
        processed_email_data = {
            'From': email_data[0],
            'Date': email_data[1],
            'Subject': email_data[2],
            'Body': preprocessed_body,
            # 'Labels': labels  # Include labels in processed data
        }
        return processed_email_data



# text_processor = TextProcessor()
# gmail_api = GmailAPI()
# email_data_list = gmail_api.get_emails(1)
# email_content_list = [(email['From'], email['Date'], email['Subject'], email['Body']) for email in email_data_list]
# data = []
# for email_data in email_content_list:
#     processed_email_data = text_processor.preprocess_email_data(email_data)
#     data.append(processed_email_data)
# print(data)
# print(len(data))
# print(type(data[0]))
