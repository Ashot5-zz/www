def colorful(num: int) -> bool:
    digits = list(map(int, str(num)))
    tmp = digits + [digits[idx - 1] * digits[idx] for idx in range(1, len(digits))]
    return len(set(tmp)) == len(tmp)


if __name__ == '__main__':
    print(263, colorful(263))
    print(236, colorful(236))
    print(23, colorful(23))
    print(5, colorful(5))
    print(55, colorful(55))
    print(94581, colorful(94581))
