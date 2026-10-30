
from pprint import pprint

from preeminence.destination import TrackTerminus

playlists_to_create = {
    "Nostalgic": "first",
    "Afro Reclaimed": "two",
    "OverDrive Reclaimed": "🙂 - the unspeakable mind.",
    "254": "Kenyan spits Reclaimed",
    "Chill Afro Reclaimed": "four",
    "Glass Hearts & Wild Fire 🧬": "Delicate emotion meets uncontrollable passion",
    "Lukas Graham Reclaimed":"seven",
    "EDM Reclaimed":"final" 
}

track_destination = TrackTerminus()
pprint(track_destination.create_playlists(playlists=playlists_to_create))