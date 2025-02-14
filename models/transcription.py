import whisper
from utils.progress_utils import ProgressBar


class Transcriber:
    def __init__(self, model_name='medium'):
        self.model = whisper.load_model(model_name)


    def transcribe(self, audio_path, output_txt_path):
        progress_bar = ProgressBar('Whisper')
        progress_bar.start()

        try:
            result = self.model.transcribe(audio_path)
            progress_bar.stop()

            with open(output_txt_path, 'w', encoding='utf-8') as f:
                f.write(result['text'])
            print(f'Transcription saved to {output_txt_path}')
        except Exception as e:
            progress_bar.stop()
            print(f'Transcription failed: {e}')
            raise
