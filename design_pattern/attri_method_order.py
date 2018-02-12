# -*- coding: utf-8 -*-
# author: willowj
#
# date: 2018-01-03 21:32:50
#

class Descdata(object):

    def __init__(self, name=''):
        self.name = name
        self.value = 0
        # 常用dict，可根据不同的instance set不同的值,get 返回不同的值
        # 相当于给每一个实例绑定了一个值

    def __get__(self, instance, owner=None):

        print("Descdata:inst> %s__get__() is called---" % self.name,
              instance, owner)
        return self.value

    def __set__(self, instance, value):
        # 定义 __delete__() 没定义 __set__()，在实例赋值 时就会报错

        print("Descdata:inst> %s __set__() is called---" % self.name,
              instance, value)
        self.value = value

    def __delete__(self, instance):
        # 定义 __set__() 没定义 __delete__()，在实例删除属性就会报错
        print('Descdata inst %s: .__delete__---'% self.name, instance)
        del self


class Desc_not_data(object):

    def __init__(self, name='', value='as654'):
        self.name = name
        self.value = value

    def __get__(self, instance, owner=None):
        print("Desc_not_data:inst> %s__get__() is called---" % self.name,
              instance, owner)
        return self.value


class Base(object):
    b_sssss = 'base_b_a'
    def __getattribute__(self, *args, **kwargs):
        print("Base __getattribute__() is called")
        return object.__getattribute__(self, *args, **kwargs)


class Test(Base):
    a = 'abc'
    d_d = Descdata(name='d_d') # 数据描述符,如果实例有同名属性 会拦截

    nd = Desc_not_data(name='nd') # 非数据描述符,如果实例有同名属性 不会拦截
    nd2 = Desc_not_data(name='nd2') # 非数据描述符,如果实例有同名属性 不会拦截


    def __init__(self, *args, **kwargs):
        self.d_d = 'Test_ins self d_d'
        #  if cls.d_d 是数据描述符,这里就是调用数据描述符的 __set__
        # 类属性name如果是数据描述符,会截断--实例ins: "self.name = value"；
        # 要是定义了 __delete__ 没定义 __set__，在实例赋值时就会报错
        self.nd2 = 'Test_>nd2' # 优先于 非数据描述符

    def __getattribute__(self, *args, **kwargs):
        print("Test  __getattribute__() is called")
        return Base.__getattribute__(self, *args, **kwargs)

    def __getattr__(self, name):
        print("Test __getattr__() is called ")
        return name + " from __getattr__"


q = Test() # init 赋值 数据描述符
# ('Descdata:inst> d_d __set__() is called---', <__main__.Test object at 0x0000000002B69DD8>, 'Test_ins self d_d')

print('-'*30,u'visit data descriptor')

print 'q.d_d\n', q.d_d, '\n'
# ('------------------------------', u'visit data descriptor')
# q.d_d
# Test  __getattribute__() is called
# Base __getattribute__() is called
# ('Descdata:inst> d_d__get__() is called---', <__main__.Test object at 0x0000000002B69DD8>, <class '__main__.Test'>)
# Test_ins self d_d

try :
    del q.d_d # # 定义 __set__() 没定义 __delete__() 就会报错
except AttributeError, e:
    print ('del q.d_d',e)
# ('del q.d_d', AttributeError('__delete__',))

print('-'*30,u'visit non data descriptor--not override')

print 'q.nd\n', q.nd, '\n'
# ('------------------------------', u'visit non data descriptor--not override')
# q.nd
# Test  __getattribute__() is called
# Base __getattribute__() is called
# ('Desc_not_data:inst> nd__get__() is called---', <__main__.Test object at 0x0000000002B69DD8>, <class '__main__.Test'>)
# as654
print('-'*30,u'visit non data descriptor--not override ')
print 'q.nd2\n', q.nd2, '\n'
# ('------------------------------', u'visit non data descriptor--not override ')
# q.nd2
# Test  __getattribute__() is called
# Base __getattribute__() is called
# Test_>nd2


print('\n q.__dict__') # call __getattribute__
print q.__dict__
#  q.__dict__
# Test  __getattribute__() is called
# Base __getattribute__() is called
# {'nd2': 'Test_>nd2'}
print('-'*30,'\n',' Test.__dict__')
a_dict_  = dict(Test.__dict__)
for k in a_dict_:
    print k,' '*(20-len(k)),a_dict_[k]


# ('------------------------------', '\n', ' Test.__dict__')
# a                     abc
# __module__            __main__
# nd                    <__main__.Desc_not_data object at 0x0000000002AA9DA0>
# __getattribute__      <function __getattribute__ at 0x0000000002AF0048>
# __getattr__           <function __getattr__ at 0x0000000002AF00B8>
# d_d                   <__main__.Descdata object at 0x0000000002AA9D30>
# nd2                   <__main__.Desc_not_data object at 0x0000000002AA9DD8>
# __doc__               None
# __init__              <function __init__ at 0x0000000002AB7F98>


print('-'*30)

print Test.__dict__['__getattribute__'] ,type(Test.__dict__['__getattribute__'])
# <function __getattribute__ at 0x0000000002B74048> <type 'function'>

print('-'*30,'class visit') # 类访问
print (Test.d_d)
# ------------------------------
# <function __getattribute__ at 0x0000000002A97F28> <type 'function'>
# ('Descdata:inst> d_d__get__() is called---', None, <class '__main__.Test'>)

print('-'*30,'class delete') # 类删除 描述符消失 #
# 类只会调用get,传入 cls, intance为空  # 不会调用描述符的 __set__ __delete__
del Test.d_d
# ('------------------------------', 'class delete')
print q.d_d # 实例描述符属性也消失
# Test  __getattribute__() is called
# Base __getattribute__() is called
# Test __getattr__() is called
