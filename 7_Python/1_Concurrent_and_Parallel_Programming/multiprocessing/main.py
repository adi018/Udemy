from multiprocessing import Process, Queue
import time

def check_value_in_list(k, i, number_of_processes, queue):
    max_num_to_check_to = 10**6
    lower = int(i * max_num_to_check_to/number_of_processes)
    upper = int((i + 1) * max_num_to_check_to/number_of_processes)
    number_of_hits = 0

    for i in range(lower, upper):
        if i in k:
            number_of_hits += 1
        # end if
    # end
    queue.put((lower, upper, number_of_hits))
# end def

num_processes = 4
comp_list = [1,2,3]
queue = Queue()

start_time = time.time()
processes = []
for i in range(num_processes):
    t = Process(target=check_value_in_list, args=(comp_list, i, num_processes, queue))
    processes.append(t)
# end

for t in processes:
    t.start()
# end

for t in processes:
    t.join()
# end

queue.put("DONE")

while True:
    v = queue.get()

    if v == "DONE":
        break
    # end if

    lower, upper, number_of_hits = v

    print(f"Between {lower} and {upper}, we have {number_of_hits} in the list")

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