import tracemalloc


def measure_memory(func, *args):

    tracemalloc.start()

    result = func(*args)

    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    memory_used = peak / 1024

    return result, round(memory_used, 2)