#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-02-08 22:34:06
#


def heap_sort(lis):
    # build big heap

    #  > x*2+1, x*2+2 : 2 > 5,6  # note : wp and down with same path
    #  < (x-1)//2 : 5,6 < 2
    for x in range(len(lis)):
        while x > 0:
            if lis[x] > lis[(x-1)//2]:
                lis[x], lis[(x-1)//2] = lis[(x-1)//2], lis[x]
            else:
                break
            x = (x-1)//2

    for x in range(len(lis)-1, 0, -1):
        # exchange biggest to the last
        print lis
        lis[0], lis[x] = lis[x], lis[0]
        # balance
        k = 0

        while x > k*2+1:
            # max child
            if k*2+2 < x and lis[k*2+2] > lis[k*2+1]:
                max_c = k*2+2
            else:
                max_c = k*2+1
            # 子节点大的 上浮，继续平衡子节点
            if lis[k] < lis[max_c]:
                lis[k], lis[max_c] = lis[max_c], lis[k]
                k = max_c
            else: # 子节点 不大于，已经平衡
                break

    return lis



