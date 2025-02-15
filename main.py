import tkinter as tk
from tkinter import filedialog
from services.video_processor import VideoProcessor

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title='Select a video/audio file for transcription',
        filetypes=[
            ('Video Files', ('*.mp4', '*.wav', '*.mkv', '*.avi', '*.mov', '*.webm', '*.flv')),
            ('Audio Files', ('*.mp3', '*.wav', '*.flac', '*.ogg', '*.aac', '*.m4a', '*.opus')),
            ('All Files', '*.*')
        ]
    )

    processor = VideoProcessor(ffmpeg_encoding='wav', model_name='medium')

    try:
        processor.process_video(file_path)
    except Exception as e:
        print(f'Error: {e}')
