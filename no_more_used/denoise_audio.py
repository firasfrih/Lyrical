import librosa
import soundfile as sf
from pydub import AudioSegment
from tkinter import Tk, filedialog

def choose_file():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(title="Choose a File", filetypes=[("WAV files", "*.wav")])
    return file_path

def choose_folder():
    root = Tk()
    root.withdraw() 
    folder_path = filedialog.askdirectory(title="Choose Output Folder")
    return folder_path

def denoise_audio(input_file, output_file, threshold=0.02):
    audio_data, sr = librosa.load(input_file)
    denoised_audio = librosa.effects.preemphasis(audio_data, coef=threshold)
    sf.write(output_file, denoised_audio, sr)

input_audio_file = choose_file()
if input_audio_file:
    output_denoised_file = choose_folder() + "/denoised_audio.wav"
    print("Processing...")
    denoise_audio(input_audio_file, output_denoised_file)
    print("Denoising completed.")