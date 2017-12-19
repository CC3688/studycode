#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ CC3688
# email:442677028@qq.com

# Python内置了很多有用的函数，我们可以直接调用   要注意 参数的个数 和 类型
#abc 求绝对值函数
a = abs(-10)
print(a)

# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误，并且Python会明确地告诉你：
# abs()有且仅有1个参数，但给出了两个

# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信
# 息：str是错误的参数类型

print(max(2,39,76,33))

# 数据类型转换  int()   float()    str()    bool()

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个
# “别名”

# hex()  把一个整数转换成 十六进制表示的 字符串

test1 = hex(89)

print(test1)
print(type(test1))

print('------定义函数-------')
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在
# 缩进块中编写函数体，函数的返回值用return语句返回

def my_abs(x):
    if x>=0:
        return x
    else :
        return -x

print(my_abs(-99))

#空函数  如果想定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass

# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代
# 码，就可以先放一个pass，让代码能运行起来。  缺少了pass，代码运行就会有语法错误

# 参数检查
# 调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
# 但是如果参数类型不对，Python解释器就无法帮我们检查。试试my_abs和内置函数abs的差别
# 当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致
# if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善
# 让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以
# 用内置函数isinstance()实现

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
# 返回多个值
# 其实这只是一种假象，Python函数返回的仍然是单一值
# 返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个
# tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便
'''
小结
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple
'''


