#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ CC3688
# email:442677028@qq.com
#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
classMates = ["Michael","Bob","Tray","Lily"]
print(classMates)
#list 长度
listLen = len(classMates)
print(listLen)
#索引从0开始,最后一个为 len()-1  或直接用-1(表示倒数第一个)  -2 表示倒数第二个,....
print(classMates[0])
print(classMates[-1])
#append(元素) 追加元素
classMates.append('CC3688')
print (classMates)
#insert(index,元素)   插入后元素的index就是这个index
classMates.insert(1,'Kevin')
print(classMates)
#pop()  删除末尾的元素  返回被删除的元素  并且 原list 减少了(最后的)一个元素
res = classMates.pop()
print(res)
print(classMates)
#pop(index)  也可以传递 一个参数,删除指定位置的元素
res = classMates.pop(1)
print(res)
print(classMates)
#直接赋值给对应的索引位置,可以把该元素替换成别的元素
classMates[0]='apple'
print(classMates)
#ist元素也可以是另一个list,可以看成是一个二维数组

#tuple  和list非常类似，但是tuple一旦初始化就不能修改
#tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple

#定义一个空的 tuble 可以写成():
t1 = ()
print(t1)
#定义一个元素的tuble 需要写成(元素,)   因为写(元素)()既可以表示tuple，又可以表示数学公式中
#的小括号，这就产生了歧义
t2 = ('onlyone',)
print(t2)
#tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一
# 个list，就不能改成指向其他对象，但指向的这个list本身是可变的

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[-1][-1])