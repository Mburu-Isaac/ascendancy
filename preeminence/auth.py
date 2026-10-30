import base64
import os
import re
import time

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class Authorization:
    
    def __init__(self):
        self.client_id =  os.environ.get("MY_CLIENT_ID")
        self.client_secret = os.environ.get("MY_CLIENT_SECRET")
        self.access_token = None
        self.expires_at = 0

    def authorization_code_flow(self):
        sp = spotipy.Spotify(
            auth_manager = SpotifyOAuth(
                client_id =self.client_id,
                client_secret = self.client_secret,
                redirect_uri = "https://example.com",
                scope = "playlist-read-private playlist-modify-private"
            )
        )
        return sp

    def get_current_user(self):
        current_user = self.authorization_code_flow().current_user()
        return current_user

    def current_user_id(self):
        current_user = self.get_current_user()

        if current_user is not None:
            return current_user["id"]

    def access_token_cache(self):
        if not self.access_token or time.time() >= (self.expires_at - 45):
            return self.request_access_token()
        return self.access_token

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
        self.access_token = response.json()["access_token"]
        self.expires_at = response.json().get("expires_in", 3600) + time.time()
        return self.access_token

    def client_credentials_flow(self):
        return self.access_token_cache()



