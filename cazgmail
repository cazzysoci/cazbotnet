import os
import base64
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def fetch_gmails(domain):
    creds = Credentials.from_authorized_user_file('credentials.json')  # Path to your Gmail API credentials file
    service = build('gmail', 'v1', credentials=creds)

    results = service.users().list(userId='me', q=f'from:*@{domain}').execute()
    messages = results.get('messages', [])

    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        payload = msg['payload']

        headers = payload['headers']
        subject = [header['value'] for header in headers if header['name'] == 'Subject'][0]
        sender = [header['value'] for header in headers if header['name'] == 'From'][0]

        parts = payload.get('parts', [])
        if len(parts) > 0:
            body = base64.urlsafe_b64decode(parts[0]['body']['data']).decode('utf-8')
        else:
            body = ''

        print(f"Subject: {subject}")
        print(f"Sender: {sender}")
        print(f"Body: {body}")
        print()

# Usage
fetch_gmails('example.com')  # Replace 'example.com' with your desired domain name
