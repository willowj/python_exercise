#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-02-09 20:59:37
#

def insert_sort(lis):

    for i in range(1, len(lis)):
        tempv = lis[i]

        for x in range(i-1, -1, -1):

            if lis[x] > tempv:
                lis[x+1] = lis[x]
                # x -= 1
            else:
                break
        # 退出循环有两种方式：lis[x] <= tempv ：插入 x+1
        # x 到 0 退出，插入 x 位置
        # 使用 for 循环 ,x不会到-1，而while 可以。
        # 这点 容易出错
        if lis[x] <= tempv:
            x+=1
        lis[x] = tempv

    return lis

print insert_sort([4, 3, 0, 2, 1])