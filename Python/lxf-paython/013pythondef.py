#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ CC3688
# email:442677028@qq.com
# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
print(fact(1))
print(fact(2))
print(fact(3))
'''
使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进
入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，
递归调用的次数过多，会导致栈溢出
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

小结
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题
'''
sum = 0
def move(n, a, b, c):
    global sum
    if n == 1:
        sum = sum +1
        print(a,'---->',c)        
    else :
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
       
    
move(4,"A","B","C")

print(sum)