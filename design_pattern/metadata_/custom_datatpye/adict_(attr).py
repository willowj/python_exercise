# -*- coding: utf-8 -*-
# author: willowj
# date: 2018-01-02 06:23:31
#
'''add attribute method to dict, with same behaviour
 any dict added in will be converted to adict '''

from __future__ import print_function
from __future__ import unicode_literals


class adict(dict):
    '''dict support attr access'''

    def __init__(self, ele_=None, **kwargs):
        self.update(ele_, **kwargs)

    def __setitem__(self, item, value):
        # ! key method !;  'dict[k] = v' will use 'self.__setitem__(k,v)'
        # not to recur , use super
        if not isinstance(value, type(self)) and isinstance(value, dict):
            value = type(self).conv(value)
        super(adict, self).__setitem__(item, value)

    def update(self, ele=None, **kwargs):
        # rewrite
        if ele:
            if hasattr(ele, "keys"):
                for k in ele:
                    self[k] = ele[k]
            else:
                for (k, v) in ele:
                    self[k] = v
        for k in kwargs:
            self[k] = kwargs[k]

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, val):
        self[attr] = val

    @classmethod
    def conv(cls, dic):
        if not isinstance(dic, dict):
            return dic
        new_dic = cls.__new__(cls)  # not trigger __init__
        for k, v in dic.iteritems():
            # __setitem__ use this, need super
            super(cls, new_dic).__setitem__(k, cls.conv(v))
        return new_dic


if __name__ == '__main__':
    print('>> any dict in will be converted to adict<<\n')
    d = adict({'j': [0]}, a=9, b={'p': 5})  # creat a adict
    print(d, '\n', type(d), type(d.b))  # subdict is also adict
    d.z = {'g': 6}  # setitem
    print(type(d.z), 'd.z.g:', d.z.g)

    d.update({'kk': {'ko': 76}})  # update to adict
    print(type(d.kk), 'd.kk.ko:', d.kk.ko, )

    #----##->----------------------------------------
    #----same as dict, shadow copy first level self-type container
    print('-.'*30)
    a = {1: 9, 'a': {u'p': 9}, 'b': [u'as']}
    b = adict(a)
    print('b is adict(b):', b is adict(b))  # False, same as dict
    # a is dict(a)
    # Out[263]: False
    print('-'*30)
    dic = dict(a)
    print([a[k] is dic[k] for k in a.keys()])
    adic = adict(b)
    print([b[k] is adic[k] for k in b.keys()])

    #----same as dict need pass iterable object
    # ->----------------------------------------
    #  d = adict(9) # 'int' object is not iterable
    # dict(range(5))
    # TypeError: cannot convert dictionary update sequence element \
    # 0 to a sequence

    z = zip('abcde', 'xiang')
    z = adict(z)
    print(z)
    print(z.d)
