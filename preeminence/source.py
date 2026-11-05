import time

from .auth import Authorization

authorization = Authorization()

class SourceTracks:
   
   def __init__(self):
      self.sp = authorization.authorization_code_flow()
      self.user_id = authorization.current_user_id()
      self.user_playlists_details = []

   def source_playlist_details(self):

      self.user_playlists_details = []

      limit = 50
      offset = 0

      while True:
         current_user_playlists = self.sp.current_user_playlists(
            limit=limit,
            offset=offset
         )

         if not current_user_playlists:
            break

         items = current_user_playlists.get("items", [])

         if not items:
            break

         self.user_playlists_details.extend(items)

         offset += limit

         if offset >= current_user_playlists["total"]:
            break

      return self.user_playlists_details

   def retrieve_playlists_ids(self, target_playlists):

      target_playlists_ids = []

      self.source_playlist_details()

      essential_playlist_data = {
         playlist.get("name"):playlist.get("id") for playlist in self.user_playlists_details if playlist and playlist.get("name")
      }

      for target_playlist_name in target_playlists:

         if target_playlist_name in essential_playlist_data:
            target_playlist_id = essential_playlist_data[target_playlist_name]
            target_playlists_ids.append(target_playlist_id)

            print(f"'{target_playlist_name}' id appended to List")

            time.sleep(2)

         else:
            print(f"playlist '{target_playlist_name}' not found in user's library")

      return target_playlists_ids

   def get_track_uris(self, playlist_id):

      playlist_tracks_data = {
         playlist_id: []
      }

      limit = 100
      offset = 0

      print("Retrieval for track URIs in the target playlists starts now ...")

      while True:
         playlist_item = self.sp.playlist_tracks(
            playlist_id=playlist_id,
            limit=limit,
            offset=offset
         )

         if not playlist_item:
            break

         items = playlist_item.get("items", []) 

         if not items:
            break

         for item_entity in items:
            track_item = item_entity.get("item")

            if track_item and track_item.get("uri"):
               playlist_tracks_data[playlist_id].append(track_item.get("uri"))

         if not playlist_item.get("next"):
            break

         offset += limit

      return playlist_tracks_data

   def retrieve_track_details(self, target_playlists):

      print("system commencing playlists details retrieval process")

      playlist_data = {}

      target_playlist_ids = self.retrieve_playlists_ids(
         target_playlists=target_playlists
      )

      if not target_playlist_ids:
         print("No valid playlist IDs found for the target playlists")

      for playlist_id in target_playlist_ids:
         if playlist_id:
            track_details = self.get_track_uris(playlist_id)
            playlist_data.update(track_details)

            time.sleep(5)

      return playlist_data

 # ["Nolstagic", "Afro","OverDrive", "254 spits", "Chill Afro", "Glass Hearts & Wild Fire 🧬👣", "Lukas Graham", "EDM"]