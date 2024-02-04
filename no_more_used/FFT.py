import numpy as np
from scipy.io import wavfile
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

def FFT(input_file, output_file, window_size=4096, hop_size=2048, threshold=1000):

    fs, audio_data = wavfile.read(input_file)
    dt = 1.0 / fs
    t = np.arange(0, len(audio_data) * dt, dt)
    signal = audio_data.astype(float)
    n = len(t)
    denoised_signal = np.zeros_like(signal)

    for i in range(0, n - window_size, hop_size):
        windowed_signal = signal[i:i + window_size]
        fhat = np.fft.fft(windowed_signal, window_size)
        psd = fhat * np.conj(fhat) / window_size
        freq = (1 / (dt * window_size)) * np.arange(window_size)
        idxs_half = np.arange(1, int(window_size / 2)).astype(int)
        psd[idxs_half[psd[idxs_half] < threshold]] = 0
        denoised_segment = np.fft.ifft(psd).real
        denoised_signal[i:i + hop_size] += denoised_segment[:hop_size]
    denoised_signal = denoised_signal.astype(np.int16)
    wavfile.write(output_file, fs, denoised_signal)

input_audio_file = choose_file()
if input_audio_file:
    output_denoised_file = choose_folder() + "/denoised_audio.wav"
    print("Processing...")
    FFT(input_audio_file, output_denoised_file)
    print("Denoising completed.")
