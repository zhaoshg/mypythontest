# coding=utf-8


def find_smallest(array):
    """
    找出数组中最小的数
    :param array:
    :return:
    """
    smallest = array[0]
    smallestIndex = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallestIndex = i
    return smallestIndex


def simple_sort(array):
    """
    简单排序，遍历找出最小的数
    :param array:
    :return:
    """
    newArr = []
    for i in range(len(array)):
        smallestIndex = find_smallest(array)
        newArr.append(array.pop(smallestIndex))
    return newArr


def bubble_sort(array):
    """
    冒泡排序
    :param array:
    :return:
    """
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] < array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
    return array


def insert_sort(array):
    """
    插入排序
    :param array:
    :return:
    """
    for i in range(1, len(array)):
        tmp = array[i]
        index = i
        while index >= 1 and array[index - 1] > tmp:
            array[index] = array[index - 1]
            index -= 1
        if index != i:
            array[index] = tmp
    return array


def shell_sort(array):
    """
    希尔排序
    :param array:
    :return:
    """
    gap = int(len(array) / 2)
    newarr = array[:]
    while gap:
        for i in range(len(array)):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            if j != i:
                array[j] = temp
        gap = int(gap / 2)
    return array


def quick_sort(array):
    """
    快速排序
    :param array:
    :return:
    """
    if len(array) < 2:
        return array
    else:
        qivot = array[0]
        less = [i for i in array[1:] if i <= qivot]
        greater = [i for i in array[1:] if i > qivot]
    return quick_sort(less) + [qivot] + quick_sort(greater)
