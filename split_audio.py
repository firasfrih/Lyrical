from pydub import AudioSegment
import os
from tkinter import Tk, filedialog

def choose_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Choose a File", filetypes=[("mp3 files", "*.mp3")])
    return file_path

def choose_folder():
    root = Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title="Choose Output Folder")
    return folder_path

def split_audio(input_file, output_folder, segment_length=10):
    # Load the input audio file
    audio = AudioSegment.from_mp3(input_file)
    # Calculate the total number of segments
    total_segments = len(audio) // (segment_length * 1000)
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Decompose the audio into 10-second segments
    for i in range(total_segments):
        start_time = i * segment_length * 1000
        end_time = (i + 1) * segment_length * 1000
        segment = audio[start_time:end_time]
        # Save each segment to the output folder
        output_file = os.path.join(output_folder, f"segment_{i + 1}.wav")
        segment.export(output_file, format="wav")

if __name__ == "__main__":
    input_file = choose_file()
    output_folder = choose_folder()
    if input_file and output_folder:
        split_audio(input_file, output_folder)
