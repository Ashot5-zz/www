def find(highstack: str, needle: str, last: bool=False) -> int:
    if last:
        xrange = range(len(highstack) - 1, 0, -1)
    else:
        xrange = range(len(highstack))

    for idx in xrange:
        if highstack[idx] == needle:
            return idx
    return -1


if __name__ == '__main__':
    print(find('first string', 's'))  # 3
    print(find('first string', 's', True))  # 6
    print(find('first string', 'w'))  # -1
