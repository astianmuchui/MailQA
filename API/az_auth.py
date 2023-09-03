import requests


def get_access_token():
    """Gets an access token for the Microsoft Graph API."""

    url = "https://login.microsoftonline.com/common/oauth2/token"
    data = {
        "grant_type": "b2f9938b-c80d-478d-bd4f-e7b684c7bc1e",
        "client_id": "0d5f81c2-85c2-4a93-acf6-ebef8bcf20cc",
        "client_secret":"005a4ab0-b368-4537-ba85-1caf8695594d",
        "resource": "https://graph.microsoft.com/"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        # print(response.status_code)
        return None


token = get_access_token()
r = requests.get("https://graph.microsoft.com/v1.0/me/messages",
                 headers={"Authorization": "Bearer " + token})

if r.status_code == 200:
    for message in r.json():
        print(message["subject"])
else:
    print("Authentication Failed")