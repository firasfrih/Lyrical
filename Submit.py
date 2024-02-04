import sys
import lyricsgenius as lg
from Found_Song import display_lyrics


def submit(song_title):
    client_access_token = "_hkQOWY190XI6XFLZ5cTpaGTQtwGmH9g5IZg6c-rDGY-5IcmOxhlLCP4knP4790c"
    genius = lg.Genius(client_access_token)
    song = genius.search_song(song_title)
    if song is None:
        print("Song not found")
        sys.exit()
    else:
        print("Song found")
        display_lyrics(song.lyrics)
        sys.exit()

    