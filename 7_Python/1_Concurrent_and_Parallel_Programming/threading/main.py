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
    for i in range(5):
        calculate_sum_squares((i+1)*1000000)
    # end

    print("Calculating sum of squares took: ", round(time.time() - calc_start_time, 1))

    sleep_start_time = time.time()
    for i in range(1, 6):
        sleep_a_little(i)
    # end
    print("Sleeping took: ", round(time.time() - sleep_start_time, 1))

if __name__=="__main__":
    main()
