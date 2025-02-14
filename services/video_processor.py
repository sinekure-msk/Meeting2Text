import os
import ffmpeg
from models.transcription import Transcriber
from utils.file_utils import validate_file

class VideoProcessor:
    def __init__(self):
        self.transcriber = Transcriber()


    def extract_video(self, video_path, audio_path):
        try:
            ffmpeg.input(video_path).output(audio_path, acodec='mp3').run()
            print(f'Audio extracted to {audio_path}')
        except Exception as e:
            print(f'Audio extraction failed: {e}')
            raise


    def process_video(self, video_path):
        if not validate_file(video_path):
            raise FileNotFoundError(f'File {video_path} does not exist')

        base_name = os.path.splitext(video_path)[0]
        audio_path = f'{base_name}_audio.mp3'
        output_txt_path = f'{base_name}_transcription.txt'

        self.extract_video(video_path, audio_path)
        self.transcriber.transcribe(audio_path, output_txt_path)