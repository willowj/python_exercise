#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python2
# author: willowj
# date: 2018-02-06 21:51:25
#


#----##->----------------------------------------
# 维持前面的有序，二分查找当前 item的 位置
class Solution:
    """
    @param: A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def countOfSmallerNumberII(self, A):
        # write your code here
        lower_item = [0]*len(A)  # 返回的列表
        z = []  # 维持前面 item 的 有序
        for i, v in enumerate(A):
            if i == 0: #  0
                z.append(v)
                continue

            up_ = i-1
            low_ = 0
            mid = (up_ + low_)//2
            while up_ > low_:
                if v > z[mid]:
                    low_ = mid+1
                elif v < z[mid]:
                    up_ = mid-1
                else:
                    break
                mid = (up_ + low_)//2

            pos = mid + int(v > z[mid])
            pos = 0 if (pos < 0) else pos
            z.insert(pos, v)

            while pos > 0 and z[pos-1] >= v:
                pos -= 1 #  除去相同项
            lower_item[i] = pos
            print z, pos, v
        return lower_item

x = Solution()
# x.countOfSmallerNumberII([1,2,7,8,5,9])
# x.countOfSmallerNumberII([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41])
x.countOfSmallerNumberII([26, 78, 27])
x.countOfSmallerNumberII([68, 64, 53, 43, 38, 3])
