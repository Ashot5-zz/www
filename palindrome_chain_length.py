def palindrome_chain_length(n: int) -> int:
    steps = 0
    while n != int(str(n)[::-1]):
        n += int(str(n)[::-1])
        steps += 1
    return steps


if __name__ == '__main__':
    print(palindrome_chain_length(87))
    print(palindrome_chain_length(923))
