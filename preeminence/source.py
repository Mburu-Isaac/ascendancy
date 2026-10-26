from .auth import Authorization
from pprint import pprint

authorization = Authorization()

class SourceTracks:
   
   def __init__(self):
      self.authorize = authorization.sp
      self.user_playlists = []
      self.target_playlists_ids = []

   def get_target_playlists(self):

      limit = 50
      offset = 0

      while True:
         current_user_playlists = self.authorize.current_user_playlists(limit=limit, offset=offset)
         items = current_user_playlists["items"]

         if not items:
            break

         self.user_playlists.extend(items)
         offset += limit

         if offset >= current_user_playlists["total"]:
            break

      playlist_names = []
      for playlist in self.user_playlists:
         playlist_names.append(playlist["name"])

      return playlist_names



   def retrieve_playlist_ids(self, target_playlists):

      for target_name in tuple(target_playlists):
         print(self.get_target_playlists().index(target_name))

      # pprint(self.user_playlists)

      

source = SourceTracks()
pprint(source.get_target_playlists())
source.retrieve_playlist_ids(
   target_playlists = ["Nolstagic", "Afro", "OverDrive", "254 spits", "Chill Afro", "Glass Hearts & Wild Fire 🧬👣", "Lukas Graham", "EDM"]
)