#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-02-08 19:53:03
#

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


#----buble soer##->----------------------------------------


def buble_sort(lis):
    # 大数后移
    for i in range(len(lis)-1):
        for x in range(len(lis)-1 - i):
            if lis[x] > lis[x+1]:
                lis[x], lis[x+1] = lis[x+1], lis[x]
    return lis

test(buble_sort)

#----insert_sort##->----------------------------------------


def insert_sort(lis):
    for i in range(1, len(lis)):
        tempv = lis[i]
        x = i-1
        while x >= 0 and lis[x] > tempv:
            lis[x+1] = lis[x]
            x -= 1
        lis[x+1] = tempv

    return lis
test(insert_sort)


def insert_sort_for(lis):

    for i in range(1, len(lis)):
        tempv = lis[i]
        for x in range(i-1, -1, -1):
            if lis[x] > tempv:
                lis[x+1] = lis[x]
            else:
                break
        # 退出循环有两种方式：
        #   lis[x] <= tempv ：插入 x+1
        #   x 到 0 退出，插入 x (0) 位置
        # 使用 for 循环 ,x不会到-1，而while 可以。
        # 这点 容易出错
        if lis[x] <= tempv:
            x += 1
        lis[x] = tempv

    return lis

test(insert_sort_for)
#----select-sort##->----------------------------------------


def select_sort(lis):
    # 记录最小 index，最后交换
    for i in range(len(lis)-1):
        min_ = i
        for x in range(i+1, len(lis)):
            if lis[x] < lis[min_]:
                min_ = x
        lis[i], lis[min_] = lis[min_], lis[i]
    return lis


def select_sort_ex(lis):
    # 直接交换 方式
    for i in range(len(lis)-1):
        for x in range(i+1, len(lis)):
            if lis[x] < lis[i]:
                lis[x], lis[i] = lis[i], lis[x]
    return lis

test(select_sort)
test(select_sort_ex)
#----quick_sort##->----------------------------------------


def quick_sort(lis, left=None, right=None):

    l_ = left = left if (left is not None) else 0
    r_ = right = right if (right is not None) else len(lis)-1
    # 不要用 right = right or len(),这样的写法
    # 这样传入 right=0 _>right =len() --- 导致无限递归
    if left >= right:
        return lis
    while l_ < r_:
        while l_ < r_ and lis[left] <= lis[r_]:
            r_ -= 1
        while l_ < r_ and lis[left] >= lis[l_]:
            l_ += 1
        # 交换 右边小于 左边大于
        lis[r_], lis[l_] = lis[l_], lis[r_]

    # 初始位置 l_ = left, 不要+1，否则 已经有序会被打乱
    lis[left], lis[l_] = lis[l_], lis[left]

    quick_sort(lis, left=left, right=l_-1)
    quick_sort(lis, left=l_+1, right=right)
    return lis

test(quick_sort)
#----heap_sort##->----------------------------------------


def heap_sort(lis):
    # build big heap

    #  >> x*2+1, x*2+2 : 2   >> 5,6  # caution : up and down with same path
    #  << (x-1)//2     : 5,6 <<  2
    for x in range(len(lis)):
        while x > 0:
            if lis[x] > lis[(x-1)//2]:
                lis[x], lis[(x-1)//2] = lis[(x-1)//2], lis[x]
            else:
                break
            x = (x-1)//2

    for x in range(len(lis)-1, 0, -1):
        # exchange biggest to the last
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
            else:  # 子节点 不大于，已经平衡
                break

    return lis

test(heap_sort)
#----merge_sort##->----------------------------------------

# 二路归并排序


def merge_(lis1, lis2):
    result = []
    k1 = k2 = 0
    while k1 < len(lis1) and k2 < len(lis2):
        if lis1[k1] <= lis2[k2]:
            result.append(lis1[k1])
            k1 += 1
        else:
            result.append(lis2[k2])
            k2 += 1
    result.extend(lis1[k1:])
    result.extend(lis2[k2:])
    return result

# 多路归并


def merge(*lis1):
    lis1 = list(lis1)
    result = []
    lis_w_ix = [0]*len(lis1)
    while 1:

        min_i = 0  # 初始最小值 来源 数组
        while min_i < len(lis1) and lis_w_ix[min_i] >= len(lis1[min_i]):
            min_i += 1  # 该数组 lis_w_ix[min_i] 元素已经遍历 完，则至下一 数组
        if min_i >= len(lis1):
            break  # 所有数组 都已经遍历完，已完结 break

        min_v = lis1[min_i][lis_w_ix[min_i]]

        for i, x in enumerate(lis1):
            if lis_w_ix[i] >= len(lis1[i]):
                continue
            if x[lis_w_ix[i]] < min_v:
                min_i = i
                min_v = x[lis_w_ix[i]]

        result.append(min_v)
        lis_w_ix[min_i] += 1

    return result

# 归并 排序


def merge_sort(lis):
    if len(lis) < 2:
        return lis

    mid = len(lis)//2

    left = merge_sort(lis[:mid])
    right = merge_sort(lis[mid:])
    return merge(left, right)

test(merge_sort)

#----shell_sort##->----------------------------------------


def shell_sort_ex(lis, step=None):
    # 交换方式 插入
    step = len(lis)//2
    while step:
        for s_ in range(step):
            # 每一子列
            while s_ + step < len(lis):
                # 此列从前往后
                z = s_
                while z >= 0:
                    # 小的往前交换
                    if lis[z] > lis[z+step]:
                        lis[z], lis[z+step] = lis[z+step], lis[z]
                        z -= step
                    else:
                        break

                s_ += step

        step //= 2
    return lis


def shell_sort(lis):
    # 插入方式
    step = len(lis)//2
    while step:
        for s_ in range(step):
            # 每一列插入 排序
            for x in range(s_, len(lis), step):
                # 此列从前往后比较， 大的都后移一位
                tempv = lis[x]
                while x-step >= s_ and lis[x-step] > tempv:
                    lis[x] = lis[x-step]
                    x -= step

                lis[x] = tempv  # 插入到最前面一个 已经移的比自己大的位置

        step //= 2
    return lis



test(shell_sort_ex)
test(shell_sort)



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

test(bucket_sort)