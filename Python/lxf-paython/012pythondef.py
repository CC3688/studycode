#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ CC3688
# email:442677028@qq.com

# 函数的参数
'''
定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只
需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者
无需了解。
Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变
参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码
'''
#位置参数
def power(x):
    return x*x 
# 此函数,参数x 就是一个位置参数
#默认参数
def power(x, n=2):
    s = 1
    while n>0:
        n=n-1
        s=s*x
    return s
#把第二个参数n的默认值设定为2 
#当高用power(4)时,就相当于调用power(5,2),而对于n>2的其他情况,
# 就必须明确的传入n power(5,3)
'''
设置默认参数时，有几点要注意：
一是必选参数在前，默认参数在后，否则Python的解释器会报错；
二是如何设置默认参数。
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
使用默认参数有什么好处？最大的好处是能降低调用函数的难度

有多个默认参数时，调用的时候，既可以按顺序提供默认参数
也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上。

定义默认参数要牢记一点：默认参数必须指向不变对象！
'''
#可变参数  在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，
# 可以是1个、2个到任意个，还可以是0个
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum =sum + n*n
    return sum
print(calc(1,2,3,4))
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数
# numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参
# 数，包括0个参数
# 已经有一个list或者tuple，要调用一个可变参数怎么办？Python允许你在list或tuple前面加一个*
# 号，把list或tuple的元素变成可变参数传进去
nums=[2,3,4,5]
print(calc(*nums))

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数#允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:',name,'age:',age,'other:',kw)

person('CC',32)
person('小陈',32,sex='man')

# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这
# 两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，
# 除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra ={'city':'Guangzhou','job':'IT'}
person('Kevin',33,**extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个
# dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# 如果要限制关键字参数的名字，就可以用命名关键字参数
def person2(name, age, *, city, job):
    print(name, age, city, job)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
person2('Jack',24,city='ShangHai',job='boss')   # 命名关键字参数 需要写参数名=...
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符
'''
参数组合
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数
都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和
关键字参数
'''
'''
小结
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*
(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 
1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''
print('----practice------')
def product(*args):
    sum = 1
    for n in args:
        sum = sum*n
    return sum
print(product(5))
print(product(5,6,7,9))



