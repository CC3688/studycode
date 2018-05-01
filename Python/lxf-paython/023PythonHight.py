#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ CC3688
# email:442677028@qq.com
#列表生成式
list = list(range(1,11))
print(list)

list2 = [x*x for x in range(1,11) if x%2==0]
print(list2)

import os
list3= [d for d in os.listdir(".")]
print(list3)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d = {'x':'A','y':'B','z':'C'}
for k, v in d.items():
    print(k,'=',v)
# 列表生成式也可以使用两个变量来生成list：
list4 = [k + '=' + v for k,v in d.items()]
print(list4)

# 最后把一个list中所有的字符串变成小写
list5 = ['Hello', 'World', 'IBM', 'Apple']
list5 = [s.lower() for s in list5]
print(list5)
print('-----------homework----------')
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

#-------------------------------
#生成器
# 列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就
# 不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成
# 器：generator

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建
# 了一个generator

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
# generator的每一个元素  可以通过next()函数获得generator的下一个返回值
g1 = (x*x for x in range(10))
print(g1)
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))
#了可以用for循环
g2 = (x*x for x in range(10))
for n in g2:
    print(n)
#homework


#迭代器
'''
可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象
如:isinstance([], Iterable)  //真   返回真假
'''
'''
生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出
StopIteration错误表示无法继续返回下一个值了。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
把list、dict、str等Iterable变成Iterator可以使用iter()函数
isinstance([],Iterator) //假    返回真假
isinstance(iter([],Iterator) //真   
'''

# 小结
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个
# Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的


