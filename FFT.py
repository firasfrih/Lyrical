#pip install soundfile
#pip install librosa
import soundfile as sf
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
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

    # Load the audio file
    y, sr = librosa.load(file_path)

    # Compute the short-time Fourier transform (STFT)
    D = librosa.stft(y)

    # Apply some noise reduction technique (e.g., thresholding)
    # You might need to experiment with the parameters to find the right balance
    threshold = 0.02
    D_filtered = D * (np.abs(D) >= threshold * np.max(np.abs(D)))

    # Inverse STFT to obtain the denoised signal
    y_denoised = librosa.istft(D_filtered)

    # Save the denoised audio to a new file in the specified output folder
    output_path = f"{output_folder}/output_denoised.wav"
    sf.write(output_path, y_denoised, sr)

# Run the preprocessing function
preprocess_audio()
