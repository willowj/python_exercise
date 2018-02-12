#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-02-09 14:27:46
#
from collections import Iterable

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        while self.current< self.high:
            yield self.current
            self.current += 1


    @classmethod
    def test(cls):
        cc = Counter(3, 8)
        print isinstance(cc, Iterable)
        for c in iter(cc):
            print c
        print '-'*50
        for c in cc:
            print c



class Counter2:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self):
        while self.current < self.high:
            i = self.current
            self.current += 1
            return i
        raise StopIteration


    @classmethod
    def test(cls):
        cc = Counter2(3, 8)
        print next(cc)
        for x in cc:
            print x



def shell_sort(lis, step=None):
    step =  5
    while step:
        for s_ in range(step):
            # 每一列插入 排序
            while s_ + step < len(lis):
                z = s_
                while z >= 0:
                    # print lis,step
                    if lis[z] > lis[z+step]:
                        lis[z], lis[z+step] = lis[z+step], lis[z]
                        z -= step
                    else:
                        break

                s_ += step
        step //= 2
    return lis

#----##->----------------------------------------
def insert_sort(lis):

    for i in range(1, len(lis)):
        tempv = lis[i]
        x = i-1
        while x>=0 and lis[x] > tempv:
            lis[x+1] = lis[x]
            x -= 1

        lis[x+1] = tempv

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
    return all(result)

n = 5
lis = range(n)
shuffle(lis)
insert_sort(lis)

print lis
print lis==range(n)
# print test(insert_sort)
# print test(shell_sort)