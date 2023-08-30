from auth import authenticate
from googleapiclient.discovery import build
from base64 import urlsafe_b64decode
from datetime import datetime, timedelta


credentials = authenticate()




def get_email_content(message_id, service):
    """Gets the content of a specific email using the Gmail API."""
    message = service.users().messages().get(userId='me', id=message_id, format='full').execute()
    payload = message['payload']
    headers = payload['headers']
    subject = next((header['value'] for header in headers if header['name'] == 'Subject'), 'No Subject')
    
    from_header = next((header['value'] for header in headers if header['name'] == 'From'), 'Unknown Sender')
    
    date_header = next((header['value'] for header in headers if header['name'] == 'Date'), 'Unknown Date')
    # date = format_date(date_header)
    
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


# def get_email_content(message_id, service):
#     """Gets the content of a specific email using the Gmail API."""
    
#     message = service.users().messages().get(userId='me', id=message_id, format='full').execute()
#     payload = message['payload']
#     headers = payload['headers']
    
#     # Convert headers to a dictionary for easier access
#     headers_dict = {header['name']: header['value'] for header in headers}
    
#     subject = headers_dict.get('Subject', 'No Subject')
#     from_header = headers_dict.get('From', 'Unknown Sender')
#     date_header = headers_dict.get('Date', 'Unknown Date')

#     body_data = ""
#     if 'body' in payload and 'data' in payload['body']:
#         body_data = payload['body']['data']
#         body = urlsafe_b64decode(body_data).decode('utf-8')
#     else:
#         body = "No content"

#     label_ids = message.get('labelIds', [])
    
#     return {
#         'From': from_header,
#         'Date': date_header,
#         'Subject': subject,
#         'Body': body,
#         'Labels': label_ids
#     }


def get_emails(days_ago):
    """Gets and prints the content of emails from the past specified days in the Gmail inbox using the Gmail API."""
    service = build('gmail', 'v1', credentials=credentials)
    
    # Calculate the date 'days_ago' days ago
    today = datetime.now()
    target_date = today - timedelta(days=days_ago)
    formatted_date = target_date.strftime('%Y-%m-%d')
    
    query = f'is:inbox after:{formatted_date}'
    
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])


    if not messages:
        return []  # Return an empty list if no emails found
    else:
        email_data_list = []
        for message in messages:
            message_id = message['id']
            email_data = get_email_content(message_id, service)
            email_data_list.append(email_data)
        
        return email_data_list



email_data_list = get_emails(1)
print(email_data_list)
