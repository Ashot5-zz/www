import time
import functools


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        started = time.time()
        res = func(*args, **kwargs)
        print(f'{func.__name__} time: {time.time() - started}')
        return res
    return wrapper


@timeit
def this_is_a_very_loooogn_running_function_indeed(stall: int = 10):
    time.sleep(stall)  


if __name__ == '__main__':
    this_is_a_very_loooogn_running_function_indeed(5)
    this_is_a_very_loooogn_running_function_indeed()
    this_is_a_very_loooogn_running_function_indeed(15)
