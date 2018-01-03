# -*- coding: utf-8 -*-
# author: willowj
# license: MIT
# date: 2018-01-02 06:23:31
#


from copy import copy as shallow_copy


class adict(dict):
    '''dict support attr access
    if only pass a dict,
    @param'''
    def __new__(cls, ele_=None, **kwargs):
        # if need to surport copy alterable like list.need to rewite new
        #   only pass a dict, just convert
        if ele_ and  isinstance(ele_, dict) \
                and not isinstance(ele_, cls):
            if not kwargs or (len(kwargs) == 1 and 'copy' in kwargs):
                copy = kwargs.get('copy', False)
                print 'copy', copy
                ele_2 = cls.conv(ele_, copy=copy)
                print '__new__ convert', id(ele_2.b), id(ele_2)
                return ele_2
        return super(adict, cls).__new__(cls, ele_, **kwargs)

    def __init__(self, ele_=None, **kwargs):
        #  重写了 __setitem__，update，不会出现，adict 嵌套 dict
        if ele_ is None and not kwargs:
            return
        # print dir(self)
        print 'new_ele_pass to init self', id(self['b']) , id(self), self
        print 'new_ele_pass to init ele_',id(ele_), ele_

        print type(ele_)
        if  self and ele_ and  isinstance(ele_, dict) \
                and not isinstance(ele_, type(self)):
            if not kwargs or (len(kwargs) == 1 and 'copy' in kwargs):
                print '# 已经是adict,不再update'
                return

        print 'init by update', self
        self.update(ele_, **kwargs)
        # if kwargs:
        #     kwargs = type(self).conv(kwargs)
        # super(adict, self).__init__(ele_, **kwargs)
        print 'new_ele_pass to inited self', id(self['b']) , id(self), self

    def __setitem__(self, item, value):
        # ! key method !; 不能再用 dict[k] = v,这就是self.__setitem__
        # 不能递归回去, super 上级用法
        if isinstance(value, dict) and not isinstance(value, type(self)):
            value = type(self).conv(value)
        super(adict, self).__setitem__(item, value)

    def update(self, ele=None, **kwargs):
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
        mydic = cls() # cls__new__(cls) better
        for k, v in dic.iteritems():
            # __setitem__ 调用了这里，也得super
            super(cls, mydic).__setitem__(k, cls.conv(v, copy=copy))
        return mydic


if __name__ == '__main__':

    a = {'a': {u'5': 9}, 'b': [u'as']}

    b = adict(a)# dict to adict
    print('a is b', a is b)
    print('a['b'] is b.b', a['b'] is b.b, type(b.a)) # not copy,
                                # 原dict里其他容器不变
    print 'id(b.b) ,id(b)) :' ,id(b.b) ,id(b)


    print '\n>>>>'
    ccc = adict(a, copy=True) # shadow copy , only copy container
    print('>>a['b'] is ccc.b, copy=True', a['b'] is ccc.b, type(ccc.a) )
    print 'id(ccc.b) ,id(ccc)) :' ,id(ccc.b) ,id(ccc)
    '''###

    print '\n'*5
    d = adict(a=9, b={'p': 5}) # creat a adict
    print(d, type(d), type(d.b)) # subdict is also adict

    d.z = {'g': 6} # setitem
    print(type(d.z))
    print d

    d.update({'u': {1: 99}}) # update
    print(type(d.u))

    '''

    #----same as dict need pass iterable object
    ##->----------------------------------------
    #  d = adict(9) # 'int' object is not iterable
    # dict(range(5))
    # TypeError: cannot convert dictionary update sequence element
    # 0 to a sequence









#----simple, bu not complete##->----------------------------------------

import copy

class Mydict(dict):

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, val):
        self[attr] = val

    @classmethod
    def conv(cls,dic, copy_=False):
        if not isinstance(dic,dict):
            return copy_ and copy.copy(dic) or dic
        mydic = cls()
        for k,v in dic.iteritems():
            mydic[k] = cls.conv(v, copy_=copy_)
        return mydic

a = {'a': {u'5': 9}, 'b': [u'as'],'c':6,5:5}

b = Mydict.conv(a)

print(a is b)
print(a['b'] is b.b)

b = Mydict.conv(a,copy_=True)

a['b'] is b.b