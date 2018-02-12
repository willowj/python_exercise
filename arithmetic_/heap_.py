#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-01-29 10:37:13
#
######################################################################
# 堆 可 以log(n) 的 时间复杂度 有序的 push，pop
#
# 堆适合 动态变化的有序提取数据，如 优先级队列、过滤出topN
######################################################################


def heapsort(list_):
    '''# 原地排序, 从小到大；大堆顶
    # 0*2 0*2+1 不方便表示子树，这里以 下标+1，取值赋值时再 -1
    import random
    r = []
    for x in range(1000):
        list_ = range(100)
        random.shuffle(list_)
        r.append(heapsort(list_) == range(100))
    all(r)
    '''
    # 建堆
    for i in range(2, len(list_)+1):
        # 大堆，后面的大值 上浮
        while i//2 > 0 and list_[i//2 - 1] < list_[i - 1]:
            list_[i//2 - 1], list_[i - 1] = list_[i - 1], list_[i//2 - 1]
            i //= 2

    # 依次拿出 堆顶
    for end in range(len(list_), 0, -1):
        # 堆顶换置于 末尾
        list_[0], list_[end - 1] = list_[end - 1], list_[0]

        k = 1  # 给置换的 新堆顶 与子树 平衡
        while 2*k < end:  # end 不再参与 堆平衡
            # 选择 较大的子树
            if (2*k+1 < end) and list_[2*k+1 - 1] > list_[k*2 - 1]:
                nexx_ = 2*k+1
            else:
                nexx_ = 2*k
            # 子树 大 ，则 下沉
            if list_[nexx_-1] > list_[k-1]:
                list_[nexx_-1], list_[k-1] = list_[k-1], list_[nexx_-1]
                k = nexx_
            else:
                # 子树 不大于 则已经平衡
                break
    return list_


class Heaplist(object):
    """ 包裹list的 小堆 数据结构
        # 外部使用 start with 0
        #
        # _shiftup _shiftdown 操作 内部存储数据
        # 下标0 置None，
        # 有效数据从 1 开始
    """

    def __init__(self, list_=None):
        self.data = [None]
        if list_:
            for x in list_:
                self.push(x)

    def __len__(self):
        return self.data.__len__() - 1

    def __bool__(self):
        return bool(len(self))

    @property
    def top(self):
        return self.data[1]

    @classmethod
    def nlarg(cls, lis, n=10, reverse=True):
        nl_heap = cls()
        for x in lis:
            if len(nl_heap) < n:
                nl_heap.push(x)
            elif x > nl_heap.top:
                nl_heap.pop()
                nl_heap.push(x)
        if reverse:
            for x in range(n):
                yield nl_heap.pop()
        else:
            for x in reversed(list(nl_heap)):
                yield x

    def _update_max(self, vaule):
        if self.data[0] is None:
            self.data[0] = vaule
        else:
            self.data[0] = max(self.data[0], vaule)

    def push(self, vaule):
        self.data.append(vaule)
        self._shiftup(len(self.data)-1)

    def _shiftup(self, index):

        while index//2 > 0 and self.data[index//2] > self.data[index]:
            self.data[index//2], self.data[index] = \
                self.data[index], self.data[index//2]
            index = index//2

    def _smaller_child(self, index, end):
        if index*2+1 < end and data[index*2+1] < data[index*2]:
            return index*2+1
        return index*2

    def _shiftdown(self, index, end):
        # keep sort in index in  [0,end) ;右边 开区间
        data = self.data
        end = min(end, len(data)-1)

        while index*2 < end:  # 字树平衡
            if index*2+1 < end and data[index*2+1] < data[index*2]:
                nexx_ = index*2+1
            else:
                nexx_ = index*2
            # 有大于 节点的子树，下沉置换
            if data[nexx_] < data[index]:
                data[nexx_], data[index] = data[index], data[nexx_]
                index = nexx_
            else:
                break

    def change(self, index, vaule):
        #  start at 0
        index += 1
        self.data[index] = vaule
        if index//2 > 1:
            if self.data[index] > self.data[index//2]:
                self._shiftdown(index)
            else:
                self._shiftup(index)

    def pop(self, index=0):
        index += 1
        if self.data[-1] != self.data[index]:
            self.data[index], self.data[-1] = self.data[-1], self.data[index]
            self._shiftdown(index, len(self.data)-1)
        return self.data.pop()

    def __iter__(self):
        for x in range(len(self.data)-1):
            yield self.pop()

if __name__ == '__main__':

    import random
    r = []
    for x in range(500):
        list_ = range(150)
        random.shuffle(list_)
        h = Heaplist(list_)
        r.append(list(h) == range(150))
    print all(r)

    for x in Heaplist.nlarg(list_, 5):
        print x,
    # 145 146 147 148 149
    for x in Heaplist.nlarg(list_, 5, reverse=False):
        print x,
        # 149 148 147 146 145
