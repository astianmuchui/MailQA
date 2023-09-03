import os
import requests
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


def callback():
    code = os.getenv('CODE')

    credentials, _ = Request().get_credentials(code)

    # Use the access token to make requests to the Gmail API
    gmail_service = build('gmail', 'v1', credentials=credentials)

    # Get the emails from the user's inbox
    emails = gmail_service.users().messages().list(userId='me').execute()

    print(emails)


if __name__ == '__main__':
    callback()
