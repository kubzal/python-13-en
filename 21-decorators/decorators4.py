# Example 3: Measuring function execution time
import time
import random

def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"Function {function.__name__} took {end - start:.4f} seconds.")
        return result
    return wrapper

@measure_time
def count_to_million():
    total = 0
    for i in range(1, 1_000_001):
        # print(i)
        total += 1
    return total

@measure_time
def wait_random_time():
    print("Start...")
    time.sleep(random.randint(1, 5))
    print("... End")

result = count_to_million()
print(result)

print()

wait_random_time()