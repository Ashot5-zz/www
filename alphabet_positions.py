def alphabet_position(text: str) -> str:
    return ' '.join(str(ord(c) - 96) for c in text.lower() if 96 < ord(c) < 123)


if __name__ == '__main__':
    print(alphabet_position('hello there!'))
