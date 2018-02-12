#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-02-09 12:50:57
#


class MergeHeap(object):
    """    # 多路归并 递增排序
    sort_ = MergeHeap([list1,list2..], descending=descending)
    for x in sort_:
        pass
    # python 需要 实现 __next__ 才作为生成器
    # 多路 归并可以用堆
    # 每一路 pop一个进入堆
    # yield :: pop堆顶时，堆顶时哪里路元素，哪一路补进来( 已经 遍历完则 pass)
    # 保持 每一路都有 最小（最大）元素在 堆里；这样 堆顶即是 最小(最大)
    """

    def __init__(self,  gens,key=None, descending=False):
        self.heap_v = []  # 存储 每一路top 值
        self.h_i = []
        # 存储 每一个值 来源index，与 self.heap_v 同步 push,pop
        self.is_antisort = self._init_antisort(key, descending)

        self.param_gens = gens
        self.gens = [iter(x) for x in gens]

        for i, g in enumerate(self.gens):
            value = next(g)
            self.push(value, i)

    def _init_antisort(self, key, descending):
        if key is None:
            def key(item):
                if hasattr(item, "__getitem__"):
                    return item[0]
                else:
                    return item

        if descending:  # 是否前后 反序
            return lambda x, y: key(x) < key(y)
        else:
            return lambda x, y:  key(x) > key(y)

    def shift_up(self, x):
        heap, h_i = self.heap_v, self.h_i

        while x > 0:
            if self.is_antisort(heap[(x - 1) // 2], heap[x]):
                heap[x], heap[(x - 1) // 2] = heap[(x - 1) // 2], heap[x]
                h_i[x], h_i[(x - 1) // 2] = h_i[(x - 1) // 2], h_i[x]
            else:
                break
            x = (x - 1) // 2

    def shift_down(self, k, end):
        heap, h_i = self.heap_v, self.h_i

        while (k * 2 + 1 <= end):
            if (k * 2 + 2 <= end) and \
                    self.is_antisort(heap[k * 2 + 1], heap[k * 2 + 2]):
                mini_c = k * 2 + 2
            else:
                mini_c = k * 2 + 1

            if self.is_antisort(heap[k], heap[mini_c]):
                heap[k], heap[mini_c] = heap[mini_c], heap[k]
                h_i[k], h_i[mini_c] = h_i[mini_c], h_i[k]
                k = mini_c
            else:
                break

    @property
    def top(self):
        if len(self.heap_v):
            return self.heap_v[0], self.h_i[0]
        else:
            return None,None


    def push(self, value, i):  # heap_v, value, h_i, i
        self.heap_v.append(value)
        self.h_i.append(i)
        self.shift_up(len(self.heap_v) - 1)


    def pop(self):
        # pop堆顶
        # 同时
        heap, h_i = self.heap_v, self.h_i

        if len(heap) == 1:
            v = heap.pop()
            i = h_i.pop()
            return v, i
        elif len(heap) < 1:
            return None, None

        heap[0], heap[-1] = heap[-1], heap[0]
        h_i[0], h_i[-1] = h_i[-1], h_i[0]

        self.shift_down(0, end=len(heap) - 2)

        return heap.pop(), h_i.pop()

    def replace(self, value,i): # push one,but pop the topest before push
        self.heap_v.append(value)
        self.h_i.append(i)
        return self.pop()

    def pushpop(self, value,i):
        if self.is_antisort(self.top[0], value):
            return value,i
        else:
            return self.replace(value,i )

    def __iter__(self):
        return self

    def next(self):
        # 迭代 输出 最值
        if len(self.h_i):
            top_v, i = self.top  # 即将 pop 的 值, 来源index

            try:  # 即将 pop 的来源 一个值 替换进去
                value = next(self.gens[i])
            except StopIteration:
                # 来源序列已经迭代完毕,不再push
                popv, i = self.pop()
            else:
                if self.is_antisort(top_v, value):
                    raise TypeError("%s is not sorted " % self.param_gens[i])
                popv, i = self.replace(value, i)

            return popv
        else:
            raise StopIteration

    # def __iter__(self):
    #      # 迭代 输出 最值
            # 不 实现 next 方法, 这样页可以 直接迭代
            #
    #     while len(self.h_i):

    #         popv, i = self.top  # 即将 pop 的 值, 来源index

    #         try:  #  即将 pop 的来源 push 一个最值
    #             value = next(self.gens[i])
    #         except StopIteration:
    #             pass
    #         else:
    #             if self.is_antisort(popv, value):
    #                 raise TypeError("%s is not sorted " % self.param_gens[i])
    #             self.push(value, i)

    #         popv, i = self.pop()
    #         yield popv
    #     else:
    #         raise StopIteration



#----##->----------------------------------------
if __name__ == '__main__':

    def test(n=5000, k=50, descending=False):
        z = []
        for x in range(k):
            t = range(x, n, k)
            if descending:
                t = t[::-1]
            z.append(t)

        r_ = MergeHeap(z, descending=descending)
        r = list(r_)

        rg = range(n)
        if descending:
            rg = rg[::-1]
        print r == rg
        # print isinstance(r_, )
    test()
    test(descending=True)
