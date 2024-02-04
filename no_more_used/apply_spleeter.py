import subprocess
from pydub import AudioSegment
import os
from tkinter import Tk, filedialog

def choose_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Choose a File", filetypes=[("MP3 files", "*.mp3")])
    return file_path

def choose_folder():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Choose Output Folder")
    return folder_path

def apply_spleeter(input_song_path, output_directory):
    spleeter_command = [
        'spleeter',
        'separate',
        '-i', input_song_path,
        '-p', 'spleeter:2stems',
        '-o', output_directory
    ]

    try:
        # Run the Spleeter command
        subprocess.run(spleeter_command, check=True)
        print("Spleeter processing completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running Spleeter: {e}")

input_song_path = choose_file()
output_directory=choose_folder()
apply_spleeter(input_song_path, output_directory)
