import itertools


def group_in_10s(*args):
    groups = [] if len(args) == 0 else [None] * (max(args) // 10 + 1)
    for idx, group in itertools.groupby(sorted(args), lambda item: item // 10):
        groups[idx] = list(group)
    return groups


if __name__ == '__main__':
    print(group_in_10s(10, 32, 12, 45, 36, 9, 22, 14, 4, 27))
    print(group_in_10s(4, 78, 71, 3))





