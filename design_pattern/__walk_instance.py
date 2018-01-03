# -*- coding: utf-8 -*-
# author: willowj
# license: MIT
# date: 2018-01-01 07:47:14
# walk instances

import weakref


class AB(object):
    """docstring for AB"""
    instances = []
    def __init__(self, arg=12):
        super(AB, self).__init__()
        self.arg = arg
        self.instances.append(weakref.proxy(self))


if __name__ == '__main__':

    z = []
    for x in range(5):
        z.append(AB(x))

    for ins_ in AB.instances:
        print ins_

    z.pop() # instance z[4] in  AB.instances is weakreffed
            # Reference to 0 ,no longer exists
    print len(z)
    print len(AB.instances)

    #print AB.instances[4]
    #ReferenceError: weakly-referenced object no longer exists
