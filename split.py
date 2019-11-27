def split(value: str, sep: str = ' ') -> list:
    result, idx, pos = [], 0, 0
    sep_len = len(sep)

    while idx < len(value):
        if sep == value[idx:idx + sep_len]:
            result.append(value[pos:idx])
            pos = idx + sep_len
            idx += sep_len
            continue
        idx += 1
    result.append(value[pos:idx + 1])

    return result


if __name__ == '__main__':
    print(split('  hello there   my dear friends  !!!', '   '))
    print('  hello there   my dear friends  !!!'.split('   '))
    print(split('this is   a long    text, with  multiple spaces', '  '))
    print('this is   a long    text, with  multiple spaces'.split('  '))
