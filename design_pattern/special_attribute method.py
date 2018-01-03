# -*- coding: utf-8 -*-
# author: willowj
# license: MIT
# date: 2018-01-01 23:01:41

# special method / attribute
#

#------- can't see by dir-------------------------------------------
  # class

'''###
cls.__subclasses__() # direct subclasses
cls.__bases__ # father class
cls.__mro__ # MRO  Method Resolution Order

vars(cls) ,vars(instance) # cls.__dict__()

issubclass(class,class2)
isinstance(ins, class)

'''


class A(object):
    """docstring for A"""
    def __init__(self, arg='A'):
        super(A, self).__init__()
        self.arg = arg
        self.zzzzz = None

class AB(A):
    """docstring for AB"""
    def __init__(self, arg='AB'):
        super(AB, self).__init__()
        self.arg = arg





A.__subclasses__() # return : [__main__.AB]
AB.__bases__
# Out[75]: (__main__.A,)
AB.__mro__
# Out[96]: (__main__.AB, __main__.A, object)




a1 = A()
vars(a1)
a1.__dict__
# Out[79]: {'arg': u'A', 'zzzzz': None}
vars(A)
 '''###
 Out[91]:
 dict_proxy({'__dict__': <attribute '__dict__' of 'A' objects>,
            '__doc__': u'docstring for A',
            '__init__': <function __main__.__init__>,
            '__module__': '__main__',
            '__weakref__': <attribute '__weakref__' of 'A' objects>})
 '''
