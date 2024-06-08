import time


def funcExecuteTimer(func):
    """
    Decorator to measure function execution time
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"【{func.__name__}: {end_time - start_time:.4f} sec execute】")
        return result

    return wrapper
