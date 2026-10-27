from .auth import Authorization
from pprint import pprint

authorization = Authorization()

class SourceTracks:
   
   def __init__(self):
      self.authorize = authorization.sp
      self.user_playlists = []
      self.target_playlists_ids = []

   def source_playlists_names(self):

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

      target_indexes = []

      for target_name in tuple(target_playlists):
         target_indexes.append(self.source_playlists_names().index(target_name))

      for index in target_indexes:
         target_id = self.user_playlists[index].get("id")
         self.target_playlists_ids.append(target_id)

   def get_track_ids(self, playlist_id):

      target_track_ids = []
      offset = 0
      limit = 2

      while True:

         playlist_item = self.authorize.playlist_items(
               playlist_id=playlist_id, 
               limit=limit,
               offset=offset
            )

         for item in playlist_item.get("items"):
               track_id = item.get("item").get("id")
               target_track_ids.append(track_id)

               if not playlist_item.get("next"):
                  break

               offset += limit

         return target_track_ids

   def track_details_retrieval_start(self):

      playlists_data = {}

      for playlist_id in tuple(self.target_playlists_ids):
         print(self.get_track_ids(playlist_id))
   


source = SourceTracks()
source.retrieve_playlist_ids(
   target_playlists = ["Nolstagic", "Afro", "OverDrive", "254 spits", "Chill Afro", "Glass Hearts & Wild Fire 🧬👣", "Lukas Graham", "EDM"]
)
# source.get_track_details()
source.track_details_retrieval_start()
