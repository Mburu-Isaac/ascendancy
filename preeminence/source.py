from .auth import Authorization
from pprint import pprint
import time
import requests
import time

authorization = Authorization()

class SourceTracks:
   
   def __init__(self):
      self.authorize = authorization.sp
      # self.apis_access_token = authorization.access_token_cache()
      self.playlist_ids = []

   def get_user_playlists(self):

      limit = 50
      offset = 0

      user_playlists = []

      while True:
         current_user_playlists = self.authorize.current_user_playlists(limit=limit, offset=offset)
         items = current_user_playlists["items"]

         user_playlists.extend(items)
         offset += limit

         if offset >= current_user_playlists["total"]:
            break

      return len(user_playlists)



      

source = SourceTracks()
print(source.get_user_playlists())