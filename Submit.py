import sys
import lyricsgenius as lg
from Found_Song import display_lyrics


def submit(song_title):
    client_access_token = 'API_KEY_HERE'  # Replace 'API_KEY_HERE' with actual API key
    genius = lg.Genius(client_access_token)
    song = genius.search_song(song_title)
    if song is None:
        print("Song not found")
        sys.exit()
    else:
        print("Song found")
        display_lyrics(song.lyrics)
        sys.exit()

    