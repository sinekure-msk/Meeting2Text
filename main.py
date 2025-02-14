import os
from services.video_processor import VideoProcessor

if __name__ == '__main__':
    video_file = r'D:\Streaming\Video\2025-02-14 21-55-15.mkv'
    processor = VideoProcessor()

    try:
        processor.process_video(video_file)
    except Exception as e:
        print(f'Error: {e}')
