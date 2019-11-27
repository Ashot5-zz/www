def linear_search(arr: list, item) -> int:
    ''' Pure implementation of linear search algorithm with O(n) complexity

    '''
    for index, elem in enumerate(arr):
        if elem == item:
            return index

    return -1


def binary_search(arr: list, item) -> int:
    ''' Pure implementation of binary search algorithm
    (half-interval, logarithmic, binary chop) with O(log n) complexity

    '''
    arr = sorted(arr)

    left = 0
    right = len(arr) - 1

    while left <= right:
        midpoint = (left + right) // 2
        if arr[midpoint] == item:
            return midpoint
        else:
            if item < arr[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1

    return -1


if __name__ == '__main__':
    print(linear_search(range(3, 17), 16))
    print(binary_search(range(3, 17), 16))
