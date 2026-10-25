import requests
import os
import base64

class Authentication:
    
    def __init__(self):
        self.client_id = os.environ.get("MY_CLIENT_ID")
        self.client_secret = os.environ.get("MY_CLIENT_SECRET")

    def request_access_token(self):
        credentials_to_encode = f"{self.client_id}:{self.client_secret}"
        encoded_bytes = base64.b64encode(credentials_to_encode.encode("utf-8"))
        encoded_credentials = encoded_bytes.decode("utf-8")

        headers = {
            "Authorization": f"Basic {encoded_credentials}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        payload = {
            "grant_type": "client_credentials"
        }

        url = "https://accounts.spotify.com/api/token"

        response = requests.post(
            url=url,
            headers=headers,
            data=payload
        )

        response.raise_for_status()
        return response.json()


client_auth = Authentication()
print(client_auth.request_access_token())