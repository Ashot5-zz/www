def decode(binstr: str) -> str:
    return ''.join(chr(int(binstr[idx:idx + 8], 2)) for idx in range(0, len(binstr), 8))


def encode(txt: str) -> str:
    return ''.join(f"{ord(ch):08b}" for ch in txt)


if __name__ == '__main__':
    binstr = encode("Rules of Optimization: Rule 1: Don't do it. Rule 2 (for experts only): Don't do it yet. - Michael A. Jackson")
    print(decode(binstr))
