"""
>>> test_map()
[1, 4, 9, 16]
>>> test_filter()
[1, 3]
>>> test_reduce1()
24
>>> test_reduce2()
24
"""

import os
import functools
import operator


def test_map():
    """
    映射处理中，以一个函数和一个iterable为参数，产生一个新的iterable，
    其中每一项都是对原始iterable中相应调用该函数所产生的结果。
    """
    return list(map(lambda x: x**2, [1, 2, 3, 4]))


def test_filter():
    """
    过滤处理以一个函数和一个iterable为参数，并生成一个新的iterable，
    其中每一项都来自原始的iterabel——假定在相应项上调用函数时返回True
    """
    return list(filter(lambda x: x > 0, [1, -2, 3, -4]))


def test_reduce1():
    """
    降低处理以一个函数和一个iterable为参数，并产生单一的结果值。
    其具体过程是：对iterable的头两个值调用函数，之后对计算所得结果与第三个值调用函数，
    之后对计算所得结果与第四个值调用函数，依此类推，直到所有的值都进行了处理。
    """
    return functools.reduce(lambda x, y: x*y, [1, 2, 3, 4])


def test_reduce2():
    return functools.reduce(operator.mul, [1, 2, 3, 4])


def count_pyfile1(files):
    return functools.reduce(operator.add, map(
        os.path.getsize, filter(lambda x: x.endswith('.py'), files)))


def count_pyfile2(files):
    return functools.reduce(operator.add, map(
        os.path.getsize, (x for x in files if x.endswith('.py'))))


def count_pyfile3(files):
    return functools.reduce(operator.add, (
        os.path.getsize(x)for x in files if x.endswith('.py')))


def count_pyfile4(files):
    return sum(os.path.getsize(x) for x in files if x.endswith('.py'))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
