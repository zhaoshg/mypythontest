# coding=utf-8

def count_down(n):
    """
    递减
    :param n:
    :return:
    """
    print(n)
    if n < 1:
        return
    else:
        count_down(n - 1)


def sumarr(array):
    """
    用递归实现数组所有数字求和
    :param array:
    :return int:
    """
    if len(array) == 0:
        return 0
    else:
        return array[0] + sumarr(array[1:])


def countarr(array):
    """
    用递归实现求数组元素个数
    :param array:
    :return:
    """
    if len(array) == 0:
        return 0
    else:
        return 1 + countarr(array[1:])


def findmax(array):
    """
    用递归实现找出列表最大的数字
    :param array:
    :return:
    """
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    else:
        submax = findmax(array[1:])
        return array[0] if array[0] > submax else submax


def find_gcd(a, b):
    """
    用递归找出最大公约数
    :param a:
    :param b:
    :return:
    """
    l = a if a > b else b
    s = b if a > b else a
    if s == 0 or l % s == 0:
        return s
    else:
        return find_gcd(l % s, s)
