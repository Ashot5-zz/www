import random


def bubble_sort(arr: list) -> list:
    """Pure implementation of bubble sort algorithm with O(n^2) complexity

    """
    length = len(arr)
    for i in range(length):
        for j in range(length - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insertion_sort(arr: list) -> list:
    """Pure implementation of the insertion sort algorithm with O(n^2) complexity

    """
    for index in range(1, len(arr)):
        while 0 < index and arr[index] < arr[index - 1]:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

    return arr


def rec_sort(arr: list) -> list:
    if len(arr) == 1:
        return [arr[0]]

    minimum = min(arr)
    arr.remove(minimum)

    return [minimum] + rec_sort(arr)


def tail_rec_sort(arr: list, result: list=[]) -> list:
    if len(arr) == 0:
        return None

    minimum = min(arr)
    result.append(minimum)
    arr.remove(minimum)

    tail_rec_sort(arr, result)


if __name__ == '__main__':
    collection = []
    for idx in range(20):
        collection.append(random.randint(-100, 100))

    print(collection)
    print(bubble_sort(collection))
    print(insertion_sort(collection))
