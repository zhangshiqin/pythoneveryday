# -*- coding: utf-8 -*-
'''
作者：Isabella
时间：2018/6/28
题目：逆转字符串——输入一个字符串，将其逆转并输出。

思路：

Python翻转字符串(reverse string), 一共包含5种方法, 其中第一种最简单, 即步长为-1, 输出字符串;

方法如下:

1. 简单的步长为-1, 即字符串的翻转(常用);

2. 交换前后字母的位置;

3. 递归的方式, 每次输出一个字符;

4. 双端队列, 使用extendleft()函数;

5. 使用for循环, 从左至右输出;

代码来源：https://blog.csdn.net/caroline_wendy/article/details/23438739
'''


string = 'abcdef'

def string_reverse1(string):
    return string[::-1]

def string_reverse2(string):
    t = list(string)
    l = len(t)
    for i, j in zip(range(l - 1, 0, -1), range(l // 2)):
        t[i], t[j] = t[j], t[i]
    return "".join(t)

def string_reverse3(string):
    if len(string) <= 1:
        return string
    return string_reverse3(string[1:]) + string[0]

from collections import deque

def string_reverse4(string):
    d = deque()
    d.extendleft(string)
    return ''.join(d)


def string_reverse5(string):
    return ''.join(string[i] for i in range(len(string) - 1, -1, -1))


print(string_reverse1(string))
print(string_reverse2(string))
print(string_reverse3(string))
print(string_reverse4(string))
print(string_reverse5(string))
