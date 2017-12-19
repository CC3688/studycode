#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ CC3688
# email:442677028@qq.com
#条件判断
#if
age = 20
if age >= 18 :
    print('your age is',age)
    print('adult')
#if else
age = 10
if age >= 18 :
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('adult')
#elif ---->else if python 写为elif   注意多条件判断时,条件的先后顺序.if语句从上往下判
# 断，如果在 某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 2
if age >= 18:
    print('your age is',age,'. your are an adult')
elif age >=10:
    print('your age is',age,'.Your are a teenager')
else:
    print('your age is',age,'.Your are a kid') 

#input()  得到的是个字符串  可以用int() 进行转格数据类型 如果转不了就会报错
'''
birth = input('birth: ')   #参数是显示给用户看的,提示用
birth = int(birth)
if birth < 2000:
    print ("你是一个00前")
else:
    print ("你是一个00后")
'''
print ("-------homework-----")
height = 1.75
weight = 80.5
#bmi = weight/(height*height)
bmi = 17
if bmi > 32 :
    print ("严重肥胖")
elif bmi >= 28 :
    print ("肥胖")
elif bmi >=25:
    print ("过重")
elif bmi >=18.5:
    print ("正常")
else :
    print ("过轻")   
