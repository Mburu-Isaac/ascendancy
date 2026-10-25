import requests
import os
import base64
import time

class Authentication:
    
    def __init__(self):
        self.client_id = os.environ.get("MY_CLIENT_ID")
        self.client_secret = os.environ.get("MY_CLIENT_SECRET")
        self._access_token = None
        self._expires_at = 0
        self._token_type = ""

    def _access_token_cache(self):

        if not self._access_token or time.time() >= (self._expires_at - 45):
            return self._request_access_token()
        self._access_token()
    
        
    def _request_access_token(self):

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
        data = response.json()

        access_token = data.get("access_token")
        token_expiry = data.get("expires_in", 3600)
        token_type = data.get("token_type")

        self._access_token = access_token
        self._expires_at = time.time() + token_expiry
        self._token_type = token_type.title()


