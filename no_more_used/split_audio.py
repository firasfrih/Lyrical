from pydub import AudioSegment
import os
from tkinter import Tk, filedialog

def choose_file():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(title="Choose a File", filetypes=[("mp3 files", "*.wav")])
    return file_path

def choose_folder():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Choose Output Folder")
    return folder_path

def split_audio(input_file, output_folder, segment_length=10):
    audio = AudioSegment.from_mp3(input_file)
 
    total_segments = len(audio) // (segment_length * 1000)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(total_segments):
        start_time = i * segment_length * 1000
        end_time = (i + 1) * segment_length * 1000
        segment = audio[start_time:end_time]

        output_file = os.path.join(output_folder, f"segment_{i + 1}.wav")
        segment.export(output_file, format="wav")

if __name__ == "__main__":
    input_file = choose_file()
    output_folder = choose_folder()
    if input_file and output_folder:
        split_audio(input_file, output_folder)
