import random


def max_by_digits(arr: list) -> int:
    tmp = []
    for item in arr:
        tmp.append(sum(map(int, str(item))))

    local = tmp[0]
    idx = 0
    for i in range(1, len(tmp)):
        if tmp[i] > local:
            local = tmp[i]
            idx = i

    return arr[idx]


arr = random.sample(range(10, 30), 5)
print(arr)
print(max_by_digits(arr))
print(max(arr, key=lambda x: sum(map(int, str(x)))))
