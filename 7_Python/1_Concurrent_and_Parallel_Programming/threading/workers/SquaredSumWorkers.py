import threading

class SquaredSumWorker(threading.Thread):
    def __init__(self, n, **kwargs):
        self._n = n
        # Initializes all the Classes from which SquaredSumWorker inherits
        super(SquaredSumWorker, self).__init__(**kwargs)
        self.start()

    # Internal Method so _ is used before function name
    def _calculate_sum_squares(self):
        sum_squares = 0
        for i in range(self._n):
            sum_squares += i ** 2
        # end

        print(sum_squares)

    def run(self):
        # with this run method we overwrite the run method of threading.Thread
        # This run(self) is trigerred by self.start()
        self._calculate_sum_squares()