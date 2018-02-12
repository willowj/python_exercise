#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-02-10 22:16:55
#

#
#----bucket_sort##->----------------------------------------

def bucket_sort(lis):

    divd_ = 1
    while  1:
        bucket_lis = [[] for x in range(10)]
        # 不要用 bucket_lis=[[]]*10 (子项 是同一引用)

        for x in lis: # 对 当前位 排序 : 当前位 是几 就放进 第几个桶里
            bucket_lis[x//divd_ % 10].append(x)

        if any(bucket_lis[1:]): # 如果 有当前位 非0 的,展开桶 继续排高一位；
                                # 没有，则已经排完所有位 break
            k = 0
            for buck in bucket_lis: # 平展开 桶
                for x in buck:
                    lis[k] = x
                    k += 1

            divd_ *= 10 # 进一位比较
        else:
            break
    return lis


from random import shuffle
import pdb


def test(sort_f, n=1000):
    result = []
    for x in range(20):
        lis = range(n)
        shuffle(lis)
        zz = sort_f(lis)
        if zz is None:
            zz = lis
        result.append(zz == range(n))
    t = all(result)
    print t, sort_f.__name__
    return t
test(bucket_sort)