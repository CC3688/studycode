#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ CC3688
# email:442677028@qq.com
#循环
#for in   可以把list 和tuple 中的每个元素迭代出来
names = ["小明","小红","CC3688","CC"]
for name in names:
    print(name)
#range() 函数可以生成一个整数序列 如果只传一个参数,就是序列的个数,从0开始,到参数减1,
#range(5) --> 0,1,2,3,4
#如果有两个参数,第一个表示起始的数,直到第二个参数减1 结束  range(2,5)-->2,3,4
sum = 0
for x in range(101):
    sum = sum +x
print(sum)

# while 循环    只要条件满足 就不断循环
sum = 0
n = 99
while n > 0 :
    sum = sum +n
    n = n -2
print(sum)
#练习
L = ["Bart","Lisa","Adam"]
for val in L :
    print("Hello,",val,"!")
#break 可以提前退出循环
n = 1
while n <= 100 :
    print(n)
    n = n +1
print("end")

m = 1
while m <= 100 :
    if m > 11:
        break
    print(m)
    m = m +1    
print("end")
#continue 跳过当前的这次循环  直接开始下一次
num = 0
while num <10:
    num = num +1
    if num %2 == 0 :
        continue
    print(num)

'''
break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句
'''