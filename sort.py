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

    排序过程：  7 2 5 4 3
    i=1:  7 _ 5 4 3 --> _ 7 5 4 3 --> 2 7 5 4 3
    i=2:  2 7 _ 4 3 --> 2 _ 7 4 3 --> 2 5 7 4 3
    i=3:  2 5 7 _ 3 --> 2 5 _ 7 3 --> 2 _ 5 7 3 --> 2 4 5 7 3
    i=4:  2 4 5 7 _ --> 2 4 5 _ 7 --> 2 4 _ 5 7 --> 2 _ 4 5 7 --> 2 3 4 5 7
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


index = 0


def quick_sort_mid(array):
    """
    快速排序，选中间一个元素为中值
    :param array:
    :return:
    XX
    """
    if len(array) < 2:
        return array
    else:
        mid = int(len(array) / 2)
        qivot = array[mid]
        less = [i for i in array[0:mid] if i <= qivot] + [i for i in array[mid + 1:] if i <= qivot]
        greater = [i for i in array[0:mid] if i > qivot] + [i for i in array[mid + 1:] if i > qivot]
    return quick_sort_mid(less) + [qivot] + quick_sort_mid(greater)


def quick_sort_head(array):
    """
    快速排序,选第一个元素为中值
    :param array:
    :return:
    XX
    """
    if len(array) < 2:
        return array
    else:
        qivot = array[0]
        less = [i for i in array[1:] if i <= qivot] + [i for i in array[1:] if i <= qivot]
        greater = [i for i in array[1:] if i > qivot] + [i for i in array[1:] if i > qivot]
    return quick_sort_head(less) + [qivot] + quick_sort_head(greater)


def quick_sort(arr):
    """
    模拟栈操作实现非递归的快速排序
    """
    if len(arr) < 2:
        return arr
    stack = [len(arr) - 1, 0]
    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)


def partition(arr, start, end):
    # 分区操作，返回基准线下标
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
        arr[end] = arr[start]
    # 此时start = end
    arr[start] = pivot
    return start


def select_sort(array):
    """
    选择排序：每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。
    :param array:
    :return:
    """
    count = len(array)
    for i in range(0, count):
        max_index = i
        for j in range(i + 1, count):
            if array[j] > array[max_index]:
                max_index = j
        temp = array[max_index]
        array[max_index] = array[i]
        array[i] = temp
    return array


def select_sort2(lists):
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        temp = lists[min]
        lists[min] = lists[i]
        lists[i] = temp
    return lists


if __name__ == '__main__':
    arr = [1, 98, 32, 8, 18, 12, 34, 56, 43, 3, 21, 25, 27, 4, 7, 5, 2]
    print(select_sort(arr[:]))
    # print(sort.shell_sort(arr[:]))
    # print(sort.simple_sort(arr[:]))
    # print(sort.insert_sort(arr[:]))
    # print(recursion.sumarr(arr[:]))
    # print(recursion.countarr(arr[:]))
    # print(recursion.findmax(arr[:]))
