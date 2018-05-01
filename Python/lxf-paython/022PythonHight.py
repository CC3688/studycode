#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ CC3688
# email:442677028@qq.com
#迭代    Iteration
#Python 用 for...in 来完成
#Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上 
# 如dict ,字符窜
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in 
# d.values()，如果要同时迭代key和value，可以用for k, v in d.items()
for value in d.values():
    print(value)

for k,v in d.items():
    print(k)
    print(v)

print(d.values())
print(d.items())

# 判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
from collections import Iterable
res = isinstance('abc',Iterable)
print(res)

# 对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把
# 一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A','B','C']):
    print(i, value)

# for循环里，同时引用了两个变量，在Python里是很常见的
for x, y in [(1,1),(2,4),(3,9)]:
    print(x,y)

print('------homework----')
def findMinAndMax(L):
    Min = None
    Max = None
    if len(L)>0:
        Min = L[0]
        Max = L[0]
        for value in L:
            if Min > value:
                Min = value      
            if Max < value:
                Max = value
    return (Min, Max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')