#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-02-06 10:31:16
#


#----##->----------------------------------------



class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        tree_list = [SegmentTreeNode(start, end)]
        # write your code here
        leve_start = 0
        while 1:
            length = len(tree_list)
            this_level_len = length - leve_start

            same_ok = 0
            # print ''.join([str(x) for x in tree_list[leve_start:]])

            for i in range(leve_start, length):
                x = tree_list[i]
                if x.start == x.end:
                    same_ok +=1
                    # print str(x)
                    continue

                mid = (x.start + x.end)//2

                x.left = SegmentTreeNode(x.start, mid)
                tree_list.append(x.left)

                x.right = SegmentTreeNode(mid+1, x.end)
                tree_list.append(x.right)

            if same_ok == this_level_len:
                break

            leve_start = length
        return tree_list[0]




######################################################################
### 打印版

class Node:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
    def __str__(self):
        return "[%d,%d]"%(self.start, self.end)


class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        tree_list = [Node(start, end)]
        # write your code here
        leve_start = 0
        while 1:
            length = len(tree_list)
            this_level_len = length - leve_start

            same_ok = 0
            # print ''.join([str(x) for x in tree_list[leve_start:]])

            for i in range(leve_start, length):
                x = tree_list[i]
                if x.start == x.end:
                    same_ok +=1
                    # print str(x)
                    continue
                mid = (x.start + x.end)//2
                tree_list.append(Node(x.start, mid))
                tree_list.append(Node(mid+1, x.end))

            if same_ok == this_level_len:
                break

            leve_start = length
        return ''.join([str(x) for x in tree_list])

Solution().build(1,5)
######################################################################