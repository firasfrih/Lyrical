import sys
import lyricsgenius as lg
from Found_Song import display_lyrics
from popup import display_popup


def submit(song_title , SCREEN):
    client_access_token = 'MY_API_KEY'  # Replace 'API_KEY_HERE' with actual API key
    genius = lg.Genius(client_access_token)
    song = genius.search_song(song_title)
    if song is None:
        print("Song not found")
        display_popup("Song not found. Please enter a valid title.",SCREEN)
        return 
    else:
        print("Song found")
        display_lyrics(song.lyrics)
        sys.exit()

    