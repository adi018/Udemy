import time
from workers.SquaredSumWorkers import SquaredSumWorker
from workers.SleepWorkers import SleepyWorker

def main():
    calc_start_time = time.time()

    current_threads = []
    for i in range(5):
        max_value = (i+1)*1000000
        squared_sum_workers = SquaredSumWorker(n=max_value)
        current_threads.append(squared_sum_workers)
    # end

    # STEP 3: Wait until all threads joins back
    for i in range(len(current_threads)):
        current_threads[i].join()
    # end

    print("Calculating sum of squares took: ", round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()

    current_threads = []
    for i in range(1, 6):
        sleepy_workers = SleepyWorker(seconds=i)
        current_threads.append(sleepy_workers)
    # end

    for i in range(len(current_threads)):
        current_threads[i].join()
    # end
    print("Sleeping took: ", round(time.time() - sleep_start_time, 1))

if __name__=="__main__":
    main()
