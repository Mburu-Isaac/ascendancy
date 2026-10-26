from .auth import Authorization
from pprint import pprint

authorization = Authorization()

class SourceTracks:
   
   def __init__(self):
      self.authorize = authorization.sp
      self.target_playlists_ids = []

   def get_user_playlists(self):

      limit = 50
      offset = 0

      user_playlists = []

      while True:
         current_user_playlists = self.authorize.current_user_playlists(limit=limit, offset=offset)
         items = current_user_playlists["items"]

         if not items:
            break

         user_playlists.extend(items)
         offset += limit

         if offset >= current_user_playlists["total"]:
            break

      playlist_names = [playlist["name"] for playlist in user_playlists]
      return playlist_names



      

source = SourceTracks()
pprint(source.get_user_playlists())