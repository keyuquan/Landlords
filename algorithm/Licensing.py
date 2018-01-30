#!/usr/bin/python
# encoding: utf-8

"""
模拟发牌
"""
import random

def main():
    list = ['3A', '4A', '5A']

    print(len(list), list.sort())

    # 3  4 5 6 7 8 9 10 J Q K A 小王 大王
    list_all = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,16,
                3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,16,
                3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,16,
                3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,16,
                18, 19]

    # 随机初始化三个人的牌
    list_A = []
    list_B = []
    list_C = []

    random.shuffle(list_all)

    list_C = list_all[0:17]
    list_C.sort()
    list_B = list_all[17:34]
    list_B.sort()
    list_A = list_all[34:54]
    list_A.sort()


    print(len(list_A), list_A)
    print(len(list_B), list_B)
    print(len(list_C), list_C)


if __name__ == "__main__":
    main()
