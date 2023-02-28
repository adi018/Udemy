import threading
import time


class SleepyWorker(threading.Thread):
    def __init__(self, seconds, **kwargs):
        # Initializes all the Classes from which SquaredSumWorker inherits
        super(SleepyWorker, self).__init__(**kwargs)
        self._seconds = seconds
        self.start()
    # end

    def _sleep_a_little(self):
        time.sleep(self._seconds)
    # end

    def run(self):
        self._sleep_a_little()