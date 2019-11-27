def factorial(num: int) -> int:
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result


def rec_factorial(num: int) -> int:
    if num <= 1:
        return 1
    return num * rec_factorial(num - 1)


def fib(count: int) -> list:
    result = [1, 1]
    if count < 3:
        return result
    for idx in range(1, count - 1):
        result.append(result[idx] + result[idx - 1])
    return result


def rec_fib(count: int) -> int:
    if count == 0:
        return 0
    elif count == 1:
        return 1
    else:
        return rec_fib(count - 1) + rec_fib(count - 2)


if __name__ == '__main__':
    print(rec_fib(10))
