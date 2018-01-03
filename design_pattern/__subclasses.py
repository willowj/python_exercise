# -*- coding: utf-8 -*-
# author: willowj
# license: MIT
# date: 2018-01-01 07:47:14
# walk subclasses

# core function: cls.__subclasses__()

import queue


class A(object):

    def __init__(self, ab=None, de=None):
        print 'A'
        print 'ab', ab,  '; de', de
    pass


class AB(A):

    def __init__(self):
        super(AB, self).__init__(ab="AB")
        print 'AB'
    pass


class DE(A):

    def __init__(self):
        super(DE, self).__init__(de='DE')
        print 'DE'
    pass


class ABC(AB, A):  # prior inherit , level 2

    def __init__(self):
        super(ABC, self).__init__()
        print 'ABC'
    pass


class ABCe(DE, ABC):

    def __init__(self):
        super(ABCe, self).__init__()
        print 'ABCe'
    pass


class ABCD(ABC, DE):

    def __init__(self):
        super(ABCD, self).__init__()
        print 'ABCD'
    pass


class ClassName(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


def get_subclasses(cls):
    all_subcls = []
    for subclass in cls.__subclasses__():
        all_subcls.append(subclass)
        all_subcls.extend(get_subclasses(subclass))
    return all_subcls


def walk_subclasses_unique(cls):
    all_subcls = []
    will_wakl = queue.Queue()
    will_wakl.put(cls)

    pop_ed = -1
    level_width = 0
    init = True
    lev_index = []
    while not will_wakl.empty():  # width priority

        cls_ = will_wakl.get()
        pop_ed += 1

        for subclass in cls_.__subclasses__():
            if subclass not in all_subcls:
                all_subcls.append(subclass)
                will_wakl.put(subclass)
                if init:
                    level_width += 1
        init = False

        if pop_ed == level_width:
            # print '000000',cls_
            lev_index.append(pop_ed)
            print 'pop_ed', pop_ed

            level_width += will_wakl.qsize()
    print lev_index
    return all_subcls

if __name__ == '__main__':

    print get_subclasses(A)
    print walk_subclasses_unique(A)
    print DE.__subclasses__()

    a = AB()
    #z = ABCD()
