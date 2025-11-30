from functools import wraps
from time import perf_counter
import tracemalloc

def measure_performance(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start = perf_counter()
        result = function(*args, **kwargs)
        end = perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f'Function {function.__name__} took {end - start:.6f} seconds')
        print(f'Documentation: {function.__doc__}')
        print(f'Memory Usage: {current} B')
        print(f'Peak memory usage: {peak} B')
        print('-'*30)

        return result
    return wrapper

@measure_performance
def make_list1():
    """Range"""
    my_list = list(range(100000))


@measure_performance
def make_list2():
    """List comprehension"""
    my_list = [l for l in range(100000)]


@measure_performance
def make_list3():
    """Append"""
    my_list = []
    for item in range(100000):
        my_list.append(item)


@measure_performance
def make_list4():
    """Concatenation"""
    my_list = []
    for item in range(100000):
        my_list += [item]

make_list1()
make_list2()
make_list3()
make_list4()