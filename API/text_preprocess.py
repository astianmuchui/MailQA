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
        email = email_data[0]
        preprocessed_body = self.remove_html_tags(email['Body'])
        preprocessed_body = self.remove_links(preprocessed_body)

        processed_email_data = {
            'From': email['From'],
            'Date': email['Date'],
            'Subject': email['Subject'],
            'Body': preprocessed_body,
        # 'Labels': labels  # Include labels in processed data
        }
        return processed_email_data




# text_processor = TextProcessor()
# gmail_api = GmailAPI()
# emails = gmail_api.get_emails(5)

# processed_email_data_list = []

# for email_data in emails:
#     processed_email_data = text_processor.preprocess_email_data(email_data)
#     processed_email_data_list.append(processed_email_data)

# # Display the processed email data
# for processed_email_data in processed_email_data_list:
#     print(processed_email_data)




# Rewrite the code so that each email is in its own tuple
# email_list = []
# for email_data in email_data_list:
#     email = (email_data['From'], email_data['Date'], email_data['Subject'], email_data['Body'])
#     email_list.append(email)

# # Print the email list
# print(email_list)

# data = []
# for email_data in email_content_list:
#     processed_email_data = text_processor.preprocess_email_data(email_data)
#     data.append(processed_email_data)
# print(data)
# print(len(data))
# print(type(data[0]))
