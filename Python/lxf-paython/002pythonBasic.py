#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @ CC3688
# email:442677028@qq.com

#格式 化输出 %s字符串  %d整数  %f小数  %%:%
print('Hi %s, you have %d.'%('CC3688',100000))
print('%4d-%04d'%(30,10))
print('%.3f'%(3.123453))
#format() 0,1 对应()里的第0,第1个, : 表示整理或输出格式.2f 表示2位小数
str = 'Hello ,{0},成绩提高了{1:.2f}%'.format('小明',17.125)
print (str)
print ("----------")
s1 = 72
s2 = 85
res = (s2-s1)*100/s1
str2 = "{0}的成绩提高了{1:.1f}%".format('小明',res)
print(str2)
