import threading
import time
from datetime import datetime

from IPython.display import clear_output


class Spinner:
    @staticmethod
    def spinning_cursor():
        while 1:
            yield from "|/-\\"

    def __init__(self, busy=False, delay=0.1):
        self.spinner_generator = self.spinning_cursor()
        self.busy = busy
        if delay and float(delay):
            self.delay = delay
        self.start_time = None

    def spinner_task(self):
        while self.busy:
            print("[+] Running...", next(self.spinner_generator))
            print("[+] Collapsed Time...", "{0:.2f}".format((datetime.now()-self.start_time).total_seconds()), "seconds")
            clear_output(wait=True)
            time.sleep(self.delay)

    def start(self):
        self.busy = True
        self.start_time = datetime.now()
        threading.Thread(target=self.spinner_task).start()

    def stop(self):
        self.busy = False
        time.sleep(self.delay)
        clear_output()
        print("Time Taken:", "{0:.2f}".format((datetime.now()-self.start_time).total_seconds()), "seconds") #print collapsed time