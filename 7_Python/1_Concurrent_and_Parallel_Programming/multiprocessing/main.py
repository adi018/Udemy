from multiprocessing import Pool, cpu_count
import time
from functools import partial

def square(x, y):
    return x**y


num_processes   = 4
comp_list       = [1, 2, 3]
power_list      = [4, 5, 6]
addition        = 2


start_time = time.time()

num_cpu_to_use = max(1, cpu_count() - 1)
print("Num of CPUs used: ", num_cpu_to_use)

prepared_list = []
for i in range(len(comp_list)):
    prepared_list.append((comp_list[i], power_list[i]))
# end
print("List used as input: ", prepared_list)

# Pool(2) --> Pool of size 2 i.e. we can use 2 processes
with Pool(num_cpu_to_use) as mp_pool:
    result = mp_pool.starmap(square, prepared_list)
    # prepared list should be of form: [(1, 4), (2, 5), (3, 6)]
    # starmap would do: square(1, 4), square(2, 5), square(3, 6)
# end with

print("Result: ", result)






print("Time taken: ", time.time() - start_time)

"""
from multiprocessing import Pool, cpu_count


def check_number_of_values_in_range(comp_list, lower, upper):
    number_of_hits = 0
    for i in range(lower, upper):
        if i in comp_list:
            number_of_hits += 1
    return number_of_hits


num_processes = 4
comparison_list = [1, 2, 3]
lower_and_upper_bounds = [(0, 25*10**6), (25*10*6, 50*10**6),
                          (50*10**6, 75*10*6), (75*10*6, 10**8)]

num_cpu_to_use = max(1, cpu_count() - 1)

print('Number of cpus being used:', num_cpu_to_use)

prepared_list = []
for i in range(len(lower_and_upper_bounds)):
    prepared_list.append((comparison_list, *lower_and_upper_bounds[i]))

print('List to use as input:', prepared_list)
with Pool(num_cpu_to_use) as mp_pool:
    result = mp_pool.starmap(check_number_of_values_in_range, prepared_list)  # [(comp_list, lower, upper), ..]

print(result)
"""