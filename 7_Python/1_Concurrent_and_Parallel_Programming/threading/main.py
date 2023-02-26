# import time
# import os
#
# from yaml_reader import YamlPipelineExecutor
#
#
# def main():
#     pipeline_location = os.environ.get('PIPELINE_LOCATION')
#     if pipeline_location is None:
#         print('Pipeline location not defined')
#         exit(1)
#     scraper_start_time = time.time()
#
#     yamlPipelineExecutor = YamlPipelineExecutor(pipeline_location=pipeline_location)
#     yamlPipelineExecutor.start()
#     yamlPipelineExecutor.join()
#     print('Extracting time took:', round(time.time() - scraper_start_time, 1))
#
#
# if __name__ == "__main__":
#     main()

import time
import threading

def calculate_sum_squares(n):
    sum_squares = 0

    for i in range(n):
        sum_squares += i**2
    # end
    print(sum_squares)
# end

def sleep_a_little(seconds):
    time.sleep(seconds)
# end

def main():
    calc_start_time = time.time()

    current_threads = []
    for i in range(5):
        max_value = (i+1)*1000000
        # STEP 1: Initialize the thread
        t = threading.Thread(target=calculate_sum_squares, args=(max_value, ))
        # STEP 2: Start the thread
        t.start()
        current_threads.append(t)
    # end

    # STEP 3: Wait until all threads joins back
    for i in range(len(current_threads)):
        current_threads[i].join()
    # end

    print("Calculating sum of squares took: ", round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()

    current_threads = []
    for i in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(i, ))
        t.start()
        # If we put t.join() here, then it turns into sequential program as the code would wait on the current iteration\
        # t.start() to finish before going to the next iteration of the for loop. Then no use of code in line 75-77
        #
        # Something like
        # t.start()
        # t.join()

        current_threads.append(t)
    # end

    for i in range(len(current_threads)):
        current_threads[i].join()
    # end
    print("Sleeping took: ", round(time.time() - sleep_start_time, 1))

if __name__=="__main__":
    main()
