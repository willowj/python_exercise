#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: willowj
# date: 2018-01-04 11:41:08
# ref https://github.com/michaelliao/learn-python/blob/master/metaclass/simple_orm.py

from __future__ import print_function

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(meta_cls, newcls_name, bases, attrs):
        print('creat..class>',meta_cls, newcls_name, '\n',bases, attrs,'\n'+'-'*10)
        if newcls_name=='Model':
            print  ('new_ class newcls_name=Model\n','-'*30,'\n')
            return type.__new__(meta_cls, newcls_name, bases, attrs)

        print('Found model: %s' % newcls_name)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            print('-'*10,'\nattrs',k,attrs,'-'*10,'\n')
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = newcls_name # 假设表名和类名一致
        return type.__new__(meta_cls, newcls_name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            print('self[key]')
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# testing code:

class User(Model):
    def __new__(cls, *args,**kwargs):
        print('will creat_instance****\n',cls.__dict__,'\n',args,kwargs,'\n'+'*'*50)
        return super(User,cls).__new__(cls, *args,**kwargs)
    id = IntegerField('uid')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd', pas='6666')



class User2(User):
    """docstring for ClassName"""
    pw = StringField('password')
    def __init__(self, *args,**kwargs):
        super(User2, self).__init__(*args,**kwargs)


u = User2(id=1234245, name='Michael', email='test@orm.org', password='my-pwd')

