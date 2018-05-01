#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'文档注释'

__author__='xixicjw'

def bulk(self):
    print('one is bulking .......')

class Dog(object):
    def __init__(self,name):
        self.name=name
    def eat(self,food='banana'):
        print('%s is eating %s .....' % (self.name,food))

d=Dog('xixi')

choice = input('>>:').strip()

if hasattr(d,choice):
    func = getattr(d,choice)
    func('菜,饭,肉')
else:
    setattr(d,choice,bulk)
    func=getattr(d,choice)
    func(d)
