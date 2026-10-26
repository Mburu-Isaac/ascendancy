from .auth import Authorization
from pprint import pprint
import time

authorization = Authorization()

class SourceTracks:
   
   def __init__(self):
      self.authorize = authorization.sp
      self.playlist_ids = []

   def get_user_playlists(self):
      # target_playlists = []

      playlist_names = []

      current_user_playlists = self.authorize.current_user_playlists(limit=50, offset=0)
      
      while len(playlist_names) != current_user_playlists["total"]:

         current_user_playlists = self.authorize.current_user_playlists(limit=50, offset=0)

         for item in current_user_playlists["items"]:
            if item["name"] not in playlist_names:
               playlist_names.append(item["name"])


         time.sleep(5)

      return playlist_names

      

source = SourceTracks()
pprint(source.get_user_playlists())