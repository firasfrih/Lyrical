import speech_recognition as sr

def recognize_lyrics(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
     #   try:
      #      lyrics = recognizer.recognize_google(audio_data)
       #     return lyrics
      #  except sr.UnknownValueError:
       #     return "Lyrics not recognized"
       
        lyrics = recognizer.recognize_google(audio_data)
        return lyrics
