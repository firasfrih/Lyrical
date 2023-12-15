#pip install pydub   
from pydub import AudioSegment
import os
from tkinter import Tk, filedialog
from Demucs import Demucs
from Demucs import __main__

def choose_file():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(title="Choose a File", filetypes=[("MP3 files", "*.mp3")])
    return file_path

def choose_folder():
    root = Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title="Choose Output Folder")
    return folder_path

def load_demucs_model():
    # Assuming you've cloned the Demucs repository, you can directly load the model
    model = Demucs(model='demucs_extra')
    return model

def separate_audio(input_audio_path, output_folder):
    # Load the Demucs model
    model = load_demucs_model()

    # Load the input audio file
    audio = AudioSegment.from_mp3(input_audio_path)

    # Perform vocal separation
    result = model(audio.get_array_of_samples())

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the separated tracks
    vocals_path = os.path.join(output_folder, 'vocals.wav')
    accompaniment_path = os.path.join(output_folder, 'accompaniment.wav')

    vocals = AudioSegment(result['vocals'].astype('int16').tobytes(), frame_rate=audio.frame_rate, sample_width=audio.sample_width, channels=1)
    accompaniment = AudioSegment(result['accompaniment'].astype('int16').tobytes(), frame_rate=audio.frame_rate, sample_width=audio.sample_width, channels=1)

    vocals.export(vocals_path, format='wav')
    accompaniment.export(accompaniment_path, format='wav')

    print(f'Saved vocals to {vocals_path}')
    print(f'Saved accompaniment to {accompaniment_path}')

# Example usage
if __name__ == "__main__":
    input_audio_path = choose_file()
    output_folder = choose_folder()
    if input_audio_path and output_folder:
        separate_audio(input_audio_path, output_folder)
