def year_to_century(year: int) -> int:
    return (year - 1) // 100 + 1


if __name__ == '__main__':
    TESTS = (
        (2001, 21),
        (2000, 20),
        (1990, 20),
        (1900, 19)
    )

    for year, answer in TESTS:
        print(year_to_century(year) == answer)
