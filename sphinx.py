#pip install SpeechRecognition
#pip install pocketsphinx
import speech_recognition as sr

def sphinx_recognize_lyrics(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        lyrics = recognizer.recognize_sphinx(audio_data)
        return lyrics
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Sphinx error; {e}")
        return ""

