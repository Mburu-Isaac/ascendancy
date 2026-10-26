import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import base64
import time


class Authorization:
    
    def __init__(self):
        self.id = os.environ.get("MY_CLIENT_ID"),
        self.secret = os.environ.get("MY_CLIENT_SECRET"),
        self.sp = spotipy.Spotify(
            auth_manager = SpotifyOAuth(
                client_id = self.id,
                client_secret = self.secret,
                redirect_uri = "https://example.com",
                scope = "playlist-read-private"
            )
        )
        self.access_token = None
        self._token_expires_at = 0

    def access_token_cache(self):
        
        if not self.access_token or time.time() >= (self._token_expires_at - 45):
            return self._request_access_token()
        return self.access_token

    def _request_access_token(self):

        credentials_to_encode = f"{self.client_id}:{self.client_secret}"
        encoded_bytes = base64.b64.encode(credentials_to_encode.encode("utf-8"))
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

        self.access_token = access_token
        self._token_expires_at = time.time() - token_expiry

        return self.access_token



        


