from auth import authenticate
from googleapiclient.discovery import build
from base64 import urlsafe_b64decode
from datetime import datetime, timedelta

class GmailAPI:
    def __init__(self):
        self.credentials = authenticate()
        self.service = build('gmail', 'v1', credentials=self.credentials)

    def get_email_content(self, message_id):
        """Gets the content of a specific email using the Gmail API."""
        message = self.service.users().messages().get(userId='me', id=message_id, format='full').execute()
        payload = message['payload']
        headers = payload['headers']

        headers_dict = {header['name']: header['value'] for header in headers}

        subject = headers_dict.get('Subject', 'No Subject')
        from_header = headers_dict.get('From', 'Unknown Sender')
        date_header = headers_dict.get('Date', 'Unknown Date')

        body_data = ""
        if 'body' in payload and 'data' in payload['body']:
            body_data = payload['body']['data']
            body = urlsafe_b64decode(body_data).decode('utf-8')
        else:
            body = "No content"

        label_ids = message.get('labelIds', [])

        return {
            'From': from_header,
            'Date': date_header,
            'Subject': subject,
            'Body': body,
            'Labels': label_ids
        }

    def get_emails(self, days_ago):
        """Gets and prints the content of emails from the past specified days in the Gmail inbox using the Gmail API."""
        today = datetime.now()
        target_date = today - timedelta(days=days_ago)
        formatted_date = target_date.strftime('%Y-%m-%d')
        query = f'is:inbox after:{formatted_date}'

        results = self.service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])

        email_data_list = []
        for message in messages:
            message_id = message['id']
            email_data = self.get_email_content(message_id)
            email_data_list.append(email_data)

        return email_data_list

    # gmail_api = GmailAPI()
    # email_data_list = gmail_api.get_emails(2)
    # for email_data in email_data_list:
    #     print(email_data)
