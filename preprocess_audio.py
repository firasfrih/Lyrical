from pydub import AudioSegment
from pydub.playback import play
from tkinter import Tk, filedialog

def choose_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Choose a File", filetypes=[("WAV files", "*.wav")])
    return file_path

def choose_folder():
    root = Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title="Choose Output Folder")
    return folder_path

def preprocess_audio():
    # Choose an audio file using the filedialog
    file_path = choose_file()
    if not file_path:
        print("No file selected. Exiting.")
        return
    # Choose an output folder using the filedialog
    output_folder = choose_folder()
    if not output_folder:
        print("No output folder selected. Exiting.")
        return
    # Load audio file
    audio = AudioSegment.from_file(file_path)
    # Apply noise reduction
    audio = audio - 20  # Example reduction of 20dB
    # Normalize the audio
    normalized_audio = audio.apply_gain(-audio.dBFS)
    # Construct the output file path within the chosen output folder
    output_file_path = f"{output_folder}/processed_audio.wav"
    # Export the processed audio to the new file path
    normalized_audio.export(output_file_path, format="wav")
    return output_file_path
# Example usage
processed_file_path = preprocess_audio()