#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @ CC3688
# email:442677028@qq.com

# 多行文本
print('''line1
line2 
line3
''');
#布尔值在条件判断中
age=20
if age>=18:
     print('成年人')
else:
     print('小孩')

'''
变量  内存创建一个变量'abc'字符串,内存创建一个名为a的变量,并把它指向'abc',b=a,就是b也指
向'abc'
'''
a='abc'
b=a
a='XYZ'
print(b)
#常量 通常用全部大写的变量名表示常量 Python根本没有任何机制保证常量不会被改变

print(10/3)
print(9/3)
print(10//3)
print(10%3)
#练习
print("----------")
print("n =",123)
print("f =",456.789)
print("s1 =","'Hello, world'")
print("s2 =","'Hello, \\'Adam\\''")
