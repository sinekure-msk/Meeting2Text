import os
import ffmpeg
import whisper


# function for convert from video to audio
def extract_video(video_path, audio_path):
    try:
        ffmpeg.input(video_path).output(audio_path, acodec='mp3').run()
        print(f'Convert to audio succeeded')
    except Exception as e:
        print(f'Convert to audio failed')
        raise


def transcribe_audio(audio_path, output_txt_path):
    try:
        model = whisper.load_model('medium')
        print('Model loaded')

        result = model.transcribe(audio_path)
        print('Transcribe finished')

        with open(output_txt_path, 'w', encoding='utf-8') as f:
            f.write(result['text'])
        print(f'Transcription saved')
    except Exception as e:
        print('Transcribe failed')


def process_video(video_path):
    base_name = os.path.splitext(video_path)[0]
    audio_path = f'{base_name}_audio.mp3'
    output_txt_path = f'{base_name}_transcription.txt'

    extract_video(video_path, audio_path)
    transcribe_audio(audio_path, output_txt_path)


if __name__ == '__main__':
    video_file = r'D:\Streaming\Video\2025-02-06 18-22-38.mkv'

    if os.path.exists(video_file):
        process_video(video_file)
    else:
        print('File doesnt exist')