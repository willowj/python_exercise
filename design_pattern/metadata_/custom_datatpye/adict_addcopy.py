# -*- coding: utf-8 -*-
# author: willowj
# license: MIT
# date: 2018-01-02 06:23:31
#
'''add attribute method to dict, with set complete '''

# from __future__ import unicode_literals
from copy import copy as shallow_copy


class adict(dict):
    '''dict support attr access

    if only pass a dict or add pram copy, just convert to adict
    @optional param copy: if copy other alterable container'''
    def __new__(cls, ele_=None, **kwargs):  # __new__ return to self
        # !>  # to support copy, otherwise, this method can be remove
        # only pass a dict, just convert
        if ele_ and isinstance(ele_, dict) and not isinstance(ele_, cls):
            if not kwargs or (len(kwargs) == 1 and 'copy' in kwargs):
                copy = kwargs.get('copy', False)
                return cls.conv(ele_, copy=copy)
        return super(adict, cls).__new__(cls, ele_, **kwargs)

    def __init__(self, ele_=None, **kwargs):
        #  rewrite __setitem__，update method,
        # so, there is no adict containing dict
        if self:
            # and isinstance(ele_, dict)  not isinstance(ele_, type(self)):
            #  if not kwargs or (len(kwargs) == 1 and 'copy' in kwargs):
            # print '#conv ed to adict , not update'  # update
            return
        self.update(ele_, **kwargs)

    def __setitem__(self, item, value):
        # ! key method !;  'dict[k] = v' will use 'self.__setitem__(k,v)'
        # not to recur , use super
        if isinstance(value, dict) and not isinstance(value, type(self)):
            value = type(self).conv(value)
        super(type(self), self).__setitem__(item, value)

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
    def conv(cls, dic, copy=False):
        if not isinstance(dic, dict):
            return copy and shallow_copy(dic) or dic
        new_dic = cls.__new__(cls) # not trigger __init__
        for k, v in dic.iteritems():
            # __setitem__ use this, need super
            super(cls, new_dic).__setitem__(k, cls.conv(v, copy=copy))
        return new_dic



if __name__ == '__main__':

    print('>>auto complete, any dict in will to adict<<\n')
    d = adict({'j': [0]}, a=9, b={'p': 5})  # creat a adict
    print(d,'\n', type(d), type(d.b))  # subdict is also adict
    d.z = {'g': 6}  # setitem
    print(type(d.z), 'd.z.g:', d.z.g)

    d.update({'kk': {'ko': 76}})  # update all to adict
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
    # TypeError: cannot convert dictionary update sequence element
    # 0 to a sequence

    #----copy ##->----------------------------------------
    a = {5: 5, 'a': {u'p': 9}, 'b': [u'as']}
    b = adict(a)  # dict to adict ,not copy, onlt convert all subdict to adict

    print('a is b', a is b)
    print('a['b'] is b.b', a['b'] is b.b, type(b.a))
    print 'id(b.b) ,id(b)) :', id(b.b), id(b)
    print b.a.p

    print '\n>>>>'
    ccc = adict(a, copy=True)  # shadow copy , only copy first level
    print('>>a['b'] is ccc.b, copy=True', a['b'] is ccc.b, type(ccc.a))
    print 'id(ccc.b) ,id(ccc)) :', id(ccc.b), id(ccc)
    print b.a.p