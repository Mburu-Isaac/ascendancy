
from pprint import pprint

# from preeminence.destination import TrackTerminus
from preeminence.source import SourceTracks

# playlists_to_create = {
#     "Nostalgic": "first",
#     "Afro Reclaimed": "two",
#     "OverDrive Reclaimed": "🙂 - the unspeakable mind.",
#     "254": "Kenyan spits Reclaimed",
#     "Chill Afro Reclaimed": "four",
#     "Glass Hearts & Wild Fire 🧬": "Delicate emotion meets uncontrollable passion",
#     "Lukas Graham Reclaimed":"seven",
#     "EDM Reclaimed":"final" 
# }

# track_destination = TrackTerminus()
# pprint(track_destination.create_playlists(playlists=playlists_to_create))

target_playlists = ["Nolstagic", "Afro","OverDrive", "254 spits", "Chill Afro", "Glass Hearts & Wild Fire 🧬👣", "Lukas Graham", "EDM"]

source_tracks = SourceTracks()
playlist_track_details = source_tracks.retrieve_track_details(target_playlists=target_playlists)

pprint(playlist_track_details)

