#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @ CC3688
# email:442677028@qq.com

# 切片  取一个list或tuple的部分元素是非常常见的操作
# 切片后  不改变原来的list tuple   是返回一个切后的新的list tuple
#[参数1:参数2(:参数3)]   参数1,参数2 都表示 数字索引
#表示从参数1  一直取到 参数2,但不包括 参数2所在的元素
#从 0 开始,0可以省略 写[:3]
#参数也可以是负数 -1 就是最后一个,其他 类推
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L1 = L[0:3]
print('L:', L)
print('L1:', L1)
#参数3 表示要取的间隔,如果是5  表示5个取一个  如果是2 表示2个取一个
#参数1,参数2 ,不用参数也要 空占位[::3] 这个3才是第三个参数
LL=list(range(100))
# print(LL)
LL1 = LL[:10]
print('LL1:',LL1)
print('LL每个五个取一个',LL[::5])

#tuple tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操
# 作，只是操作的结果仍是tuple.   还是不改变原来的tuple  返回新的tuple
tt = (0,1,2,3,4,5,6,7)
print(type(tt))
tt1=tt[0:3]
print(type(tt1),tt1)
print(type(tt),tt)

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符,也可以用切片操作，只
# 是操作结果仍是字符串      还是不改变原来的字符串  返回新的字符串
str = "abcdefghijklm"
print(str[1])
str1 = str[0:3]
print(type(str1),str1)
print(type(str),str)

print('--------homework--------')
'''
def trim(s):
    i = 0
    sLen = len(s)
    startIndex=0
    while i < sLen:
        if s[i:i+1] !=" ":
            startIndex=i
            break
        i= i+1
    num=-1
    Long= (-sLen)
    endIndex=-1
    while num >Long:
        if s[num-1:num]!= " ":
            endIndex=num
            break
        num=num-1
   
    if startIndex == 0 and endIndex == -1:
        return ''
    elif endIndex == -1:
        return s[startIndex:]
    else:
        return s[startIndex:endIndex]
'''
def trim(s):
    while len(s) > 0 and s[0:1] == ' ':
        s = s[1:]
    while len(s) > 0 and s[-1:] == ' ':
         s = s[:-1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')




