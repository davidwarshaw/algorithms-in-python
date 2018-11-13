#!/usr/bin/env python


def _exchange(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def selection_sort(unsorted):
    exchange_count = 0
    for i in range(len(unsorted)):
        minId = i
        for j in range(i + 1, len(unsorted)):
            if unsorted[j] < unsorted[minId]:
                minId = j
        _exchange(unsorted, minId, i)
        exchange_count += 1
    print('Exchange Count: ' + str(exchange_count))


def insertion_sort(unsorted):
    exchange_count = 0
    for i in range(1, len(unsorted)):
        for j in range(i, 0, -1):
            if unsorted[j] < unsorted[j - 1]:
                _exchange(unsorted, j, j - 1)
                exchange_count += 1
    print('Exchange Count: ' + str(exchange_count))


def shell_sort(unsorted):
    h = 1
    while h < len(unsorted) // 3:
        h = (3 * h) + 1
    exchange_count = 0
    while h >= 1:
        for i in range(h, len(unsorted)):
            for j in range(i, h, -h):
                if unsorted[j] < unsorted[j - h]:
                    _exchange(unsorted, j, j - h)
                    exchange_count += 1
        h = h // 3
    print('Exchange Count: ' + str(exchange_count))


if __name__ == '__main__':
    # All out of order
    a = range(20, 0, -1)
    print(a)
    selection_sort(a)
    print(a)
    print('\n')

    # One out of order
    a = range(1, 21)
    _exchange(a, 13, 14)
    print(a)
    selection_sort(a)
    print(a)
    print('\n')

    # All out of order
    a = range(20, 0, -1)
    print(a)
    insertion_sort(a)
    print(a)
    print('\n')

    # One out of order
    a = range(1, 21)
    _exchange(a, 13, 14)
    print(a)
    insertion_sort(a)
    print(a)
    print('\n')

    # All out of order
    a = range(20, 0, -1)
    print(a)
    shell_sort(a)
    print(a)
    print('\n')

    # One out of order
    a = range(1, 21)
    _exchange(a, 13, 14)
    print(a)
    shell_sort(a)
    print(a)
    print('\n')
