import os
import ffmpeg
from models.transcription import Transcriber
from utils.file_utils import validate_file
from utils.progress_utils import ProgressBar


class VideoProcessor:
    def __init__(self, ffmpeg_encoding='mp3', model_name='medium'):
        self.transcriber = Transcriber(model_name)
        self.ffmpeg_encoding = ffmpeg_encoding

    def extract_video(self, video_path, audio_path):
        progress_bar = ProgressBar('FFmpeg')
        progress_bar.start()

        try:
            ffmpeg.input(video_path).output(audio_path, format=self.ffmpeg_encoding).global_args('-loglevel', 'error').run()
            progress_bar.stop()
        except Exception as e:
            progress_bar.stop()
            print(f'Audio extraction failed: {e}')
            raise


    def process_video(self, video_path):
        if not validate_file(video_path):
            raise FileNotFoundError(f'File {video_path} does not exist')

        base_name = os.path.splitext(video_path)[0]
        audio_path = f'{base_name}_audio.{self.ffmpeg_encoding}'
        output_txt_path = f'{base_name}_transcription.txt'

        self.extract_video(video_path, audio_path)
        self.transcriber.transcribe(audio_path, output_txt_path)