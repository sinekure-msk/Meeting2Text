import time
import threading

class ProgressBar:
    def __init__(self, process_name):
        self.process_name = process_name
        self.flag = threading.Event()
        self.progress_thread = None

    def show_progress(self):
        start_time = time.time()
        print(f'[ . . . . . {self.process_name} . . . . . ]')

        while not self.flag.is_set():
            elapsed_time = int(time.time() - start_time)
            print(f'\r[ {elapsed_time} sec. ]', end='', flush=True)
            time.sleep(1)

    def start(self):
        self.progress_thread = threading.Thread(target=self.show_progress)
        self.progress_thread.start()

    def stop(self):
        self.flag.set()
        self.progress_thread.join()