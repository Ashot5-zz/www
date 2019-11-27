import functools
from datetime import datetime


def when(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args: tuple, **kwargs: dict):
        print(f'Function "{func.__name__}" called at {datetime.now()}')
        return func(*args, **kwargs)
    return wrapper


@when
def do_something():
    return 'something is done'


if __name__ == '__main__':
    print(do_something())
    print(do_something.__name__)
