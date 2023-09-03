import base64
from auth import authenticate
from googleapiclient.discovery import build
from datetime import datetime, timedelta

def parse_msg(msg):
    if msg.get("payload").get("body").get("data"):
        return base64.urlsafe_b64decode(msg.get("payload").get("body").get("data").encode("ASCII")).decode("utf-8")
    return msg.get("snippet")

class GmailAPI:
    def __init__(self):
        self.credentials = authenticate()
        self.service = build('gmail', 'v1', credentials=self.credentials)

    def get_email_content(self, message_id):
        """Gets the content of a specific email using the Gmail API."""
        message = self.service.users().messages().get(userId='me', id=message_id, format='full').execute()
        decoded_body = parse_msg(message)

        # Extract subject, from, and date from email headers
        headers = message['payload']['headers']
        # labels = [header['value'] for header in headers if header['name'] == 'Label']
        subject = next((header['value'] for header in headers if header['name'] == 'Subject'), 'No Subject')
        from_header = next((header['value'] for header in headers if header['name'] == 'From'), 'Unknown Sender')
        date_header = next((header['value'] for header in headers if header['name'] == 'Date'), 'Unknown Date')
        # label_ids = message.get('labelIds', [])
        
        # Create email data dictionary with empty strings for missing elements
        email_data = {
            'From': from_header,
            'Date': date_header,
            'Subject': subject,
            'Body': decoded_body
            # 'Labels': label_ids,
        }
        
        return email_data

    def get_emails(self, days_ago):
        """Gets and returns the content of primary emails from the past specified days in the Gmail inbox using the Gmail API."""
        today = datetime.now()
        target_date = today - timedelta(days=days_ago)
        formatted_date = target_date.strftime('%Y-%m-%d')
        query = f'category:primary is:inbox after:{formatted_date}'

        results = self.service.users().messages().list(userId='me', maxResults=20, q=query).execute()
        messages = results.get('messages', [])

        email_data_list = []
        for message in messages:
            message_id = message['id']
            email_data = self.get_email_content(message_id)
            email_data_list.append((email_data,))
            # Each email data is now in its own tuple

        return email_data_list



# gmail_api = GmailAPI()
# email_data_list = gmail_api.get_emails(1)
# print(email_data_list)
# email_content_list = [(email['From'], email['Date'], email['Subject'], email['Body']) for email in email_data_list]

# emails=[]
# for email_content in email_content_list:
#     print("From:", email_content[0])
#     print("Date:", email_content[1])
#     print("Subject:", email_content[2])
#     print("Body:", email_content[3])
#     print()
#     emails.append(email_content)

# print(emails)
# print(len(emails))
