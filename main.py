import tkinter as tk
from tkinter import filedialog
from services.video_processor import VideoProcessor

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title='Select a video/audio file for transcription',
        filetypes=[('Video Files', ('*.mp4', '*.wav', '*.mkv')), ('Audio FIles', '*.mp3'), ('All Files', '*.*')]
    )

    processor = VideoProcessor()

    try:
        processor.process_video(file_path)
    except Exception as e:
        print(f'Error: {e}')
