import whisper

class Transcriber:
    def __init__(self, model_name='medium'):
        self.model = whisper.load_model(model_name)


    def transcribe(self, audio_path, output_txt_path):
        try:
            result = self.model.transcribe(audio_path)
            with open(output_txt_path, 'w', encoding='utf-8') as f:
                f.write(result['text'])
            print(f'Transcription saved to {output_txt_path}')
        except Exception as e:
            print(f'Transcription failed: {e}')
            raise
