#!/usr/bin/env python3
# -*- coding: utf-8 -*


# age = int(input())
# if age >= 18:
#    print('adult')
# else:
#    print('teenager')


# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

#list#list是一种有序的集合，可以随时添加和删除其中的元素。

# classmates = ['Michael', 'Bob', 'Tracy']
# print(classmates)
# print(len(classmates))
# print(classmates[0])
# print(classmates[-1])
# classmates.append('Adam')
# print(classmates)
# classmates.insert(1, 'Jack')
# print(classmates)
# classmates.pop(1)
# print(classmates)
# classmates[1] = 'Sarah'
# print(classmates)
#####################
# ['Michael', 'Bob', 'Tracy']
# 3
# Michael
# Tracy
# ['Michael', 'Bob', 'Tracy', 'Adam']
# ['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
# ['Michael', 'Bob', 'Tracy', 'Adam']
# ['Michael', 'Sarah', 'Tracy', 'Adam']

# p = ['asp', 'php']
# s = ['python', 'java', p, 'scheme']
# print(s)
# print(len(s))
# print(s[2][1])

#tuple#tuple一旦初始化就不能修改。

# classmates = ('Michael', 'Bob', 'Tracy')
# print(classmates[])

# t = ('a', 'b', ['A', 'B'])
# t[2][0] = 'X'
# t[2][1] = 'Y'
# print(t)

# age = int(input('please entry your age:'))
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# elif age >= 6:
#     print('your age is', age)
#     print('teenager')
# else:
#     print('your age is', age)
#     print('kid')

# 2018-3-22

# height = float(input('请输入身高，单位米：'))
# weight = float(input('请输入体重，单位KG：'))
# bmi = weight/height/height
# if bmi>32:
#     print('严重肥胖')
# elif bmi>28:
#     print('肥胖')
# elif bmi>25:
#     print('过重')
# elif bmi>18.5:
#     print('正常')
# else:
#     print('过轻')

# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)

# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print('Hello,',name,'!')

# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')

# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)

# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])
# d['Michael'] = 90
# print(d['Michael'])
# print('Bob' in d)
# print(d.get('Jimmy'))
# print(d.get('Jimmy',-99))
# d.pop('Bob')
# print(d)
###############
# 95
# 90
# True
# None
# -99
# {'Michael': 90, 'Tracy': 85}

# s = set([1, 1, 2, 2, 3, 3])
# print(s)
# s.add(4)
# print(s)
# s.remove(4)
# print(s)
# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# print(s1 & s2)
# print(s1 | s2)
##############
# {1, 2, 3}
# {1, 2, 3, 4}
# {1, 2, 3}
# {2, 3}
# {1, 2, 3, 4}

# a = ['c', 'b', 'a']
# a.sort()
# print(a)

# a = 'abc'
# print(a.replace('a', 'A'))
# print(a)
###############
# Abc
# abc

# ???tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。???

# print(abs(-20))
# print(max(1,2,3,4,230))
# print(int('123'))
# print(int(12.3))
# print(float('12.34'))
# print(str(1.23))
# print(bool(1))
# print(bool(''))
##################
# 20
# 230
# 123
# 12
# 12.34
# 1.23
# True
# False

# a=abs
# print(a(-1))
# print(hex(255))
# #############
# 1
# 0xff

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-3.14))

#2018-03-23

# from abstest import my_abs
# print(my_abs(-9))

# def nop():
#     pass

# age=19
# if age >= 18:
#     pass

# import math
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)
# r = move(100, 100, 60, math.pi / 6)
# print(r)

# import math
#
# def quadratic(a, b, c):
#     if not isinstance(a, (int, float)):
#             raise TypeError('bad operand type')
#     if not isinstance(b, (int, float)):
#             raise TypeError('bad operand type')
#     if not isinstance(c, (int, float)):
#             raise TypeError('bad operand type')
#     d = b * b - 4 * a * c
#     if a == 0:
#         if b == 0:
#             if c == 0:
#                 return '方程根为全体实数'
#             else:
#                 return '方程无根'
#         else:
#             x1 = -c / b
#             x2 = x1
#             return x1, x2
#     else:
#         if d < 0:
#             return '方程无根'
#         else:
#             x1 = (-b + math.sqrt(d)) / 2 / a
#             x2 = (-b - math.sqrt(d)) / 2 / a
#             return x1, x2
#
# print(quadratic(0,0,0))
# print(quadratic(0,0,1))
# print(quadratic(0,2,2))
# print(quadratic(0,0,2))
# print(quadratic(2,2,2))
# print(quadratic(1,3,-4))
# 方程根为全体实数
# 方程无根
# (-1.0, -1.0)
# 方程无根
# 方程无根
# (1.0, -4.0)

# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(power(2,8))
# print(power(2))

# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
#
# enroll('Adam', 'M', city='Tianjin')

# def add_end(L=[]):
#     L.append('END')
#     return L
# print(add_end())
# print(add_end())
#
# # 定义默认参数要牢记一点：默认参数必须指向不变对象！

# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')
#     return L
# print(add_end())
# print(add_end())

# #由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
# #但是调用的时候，需要先组装出一个list或tuple，所以，我们把函数的参数改为可变参数：
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(1,2,3,4))
# nums = [1, 2, 3,4]
# print(calc(*nums))

# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)
# print(person('Michael', 30))
# print(person('Bob', 35, city='Beijing'))
# print(person('Adam', 45, gender='M', job='Engineer'))
# print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))

# def person(name, age, *, city='Beijing', job):
#     print(name, age, city, job)
# print(person('Jack', 24, job='Engineer'))

## 参数组合
##
## 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
## 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
## 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# print(f1(1, 2))
# print(f1(1, 2, c=3))
# print(f1(1, 2, 3, 'a', 'b'))
# print(f1(1, 2, 3, 'a', 'b', x=99))
# print(f2(1, 2, d=99, ext=None))

##a = 1 b = 2 c = 0 args = () kw = {}
##a = 1 b = 2 c = 3 args = () kw = {}
##a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
##a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
##a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

##最神奇的是通过一个tuple和dict，你也可以调用上述函数：

# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)

##a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# f2(*args, **kw)

##a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

# def product(*numbers):                                              #定义一个函数
#     if numbers is None or len(numbers)<=0 :
#         raise TypeError("args not null!")                              #将函数提前给定好各种情况,如果小于零,等于零或者未输入
#     sum = 1
#     for n in numbers:
#         sum = sum *n                            #如果n在给定的数列中,那么就将sum*每一个数值得出总数
#     return sum
#
# print(product(5,3,2))

##2018-3-25

# def fact(n):
#     if n==1:
#         return 1
#     return n + fact(n - 1)
# print(fact(1000))            #递归调用栈溢出

# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num + product)
#
# print(fact_iter(1000, 1))           #尾递归做优化，也没有什么用。

# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)  # 递归结束条件
#     else:
#         move(n - 1, a, c,b)  # <span style="color:rgb(102,102,102);font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;white-space:pre-wrap;">将n-1块移动至b</span>
#         move(1, a, b,c)  # <span style="color:rgb(102,102,102);font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;line-height:20px;white-space:pre-wrap;">将最大那块移动至c</span>
#         move(n - 1, b, a,c)  # <span style="color:rgb(102,102,102);font-family:'Helvetica Neue', Helvetica, Arial, sans-serif;line-height:20px;white-space:pre-wrap;">从n-1块开始，ab参数位置对调 </span>
#
# n = int(input('请输入第一个柱子A的盘子数量：'))
# print('n=%d时的移动路线：' % n)
#
# print(move(n, 'A', 'B', 'C'))

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# r = []
# n = 3
# for i in range(n):
#     r.append(L[i])
#
# print(r)          #直接切片：print(L[0:3])‘从索引0开始取，直到索引3为止，但不包括索引3。’
# print(L[-2:-1])

# print((0, 1, 2, 3, 4, 5)[:3])

# print('ABCDEFG'[::2])

# from chatterbot import ChatBot
#
# chatbot=ChatBot("haohao")
#
#
# from chatterbot.trainers import ListTrainer
# conversation =[
# "Hello",
# "Hi there!",
# "How are you doing?",
# "I'm doing great.",
# "That is good to hear",
# "Thank you.",
# "You're welcome."
# ]
# chatbot.set_trainer(ListTrainer)
# chatbot.train(conversation)
#
# response = chatbot.get_response("Good morning!")
# print(response)

##2018-3-27

##list列表[]

# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)

# print(list(range(1, 11)))

# L = []
# for x in range(1,11):
#     L.append(x * x)
# print(L)

# print([x * x for x in range(1, 11)])

# print([x * x for x in range(1, 11) if x % 2 == 0])

# print([m + n for m in 'ABC' for n in 'XYZ'])

# import os
# print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录

# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# for k, v in d.items():
#     print(k, '=', v)

# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# print([k + '=' + v for k, v in d.items()])

# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])

##2018年4月3日

# L = [x * x for x in range(10)]
# print([L])
# g = (x * x for x in range(10))
# print(g)

# #[[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]]
# #<generator object <genexpr> at 0x0000017576564990>
# #创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
#
# for n in g:
#     print(n)

##2018-04-09
#
# str='Runoob'
#
# print(str)                 # 输出字符串
# print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
# print(str[0])              # 输出字符串第一个字符
# print(str[2:5])            # 输出从第三个开始到第五个的字符
# print(str[2:])             # 输出从第三个开始的后的所有字符
# print(str * 2)             # 输出字符串两次
# print(str + '你好')        # 连接字符串
#
# print('------------------------------')
#
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

##2018-04-12

# list = ['abcd', 786, 2.23, 'runoob', 70.2]
# tinylist = [123, 'runoob']
#
# print(list)  # 输出完整列表
# print(list[0])  # 输出列表第一个元素
# print(list[1:3])  # 从第二个开始输出到第三个元素
# print(list[2:])  # 输出从第三个元素开始的所有元素
# print(tinylist * 2)  # 输出两次列表
# print(list + tinylist)  # 连接列表

##List写在方括号之间，元素用逗号隔开。

# tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
# tinytuple = (123, 'runoob')
#
# print(tuple)  # 输出完整元组
# print(tuple[0])  # 输出元组的第一个元素
# print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
# print(tuple[2:])  # 输出从第三个元素开始的所有元素
# print(tinytuple * 2)  # 输出两次元组
# print(tuple + tinytuple)  # 连接元组

##元组写在小括号 () 里，元素之间用逗号隔开。

# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
#
# print(student)  # 输出集合，重复的元素被自动去掉
#
# # 成员测试
# if ('Rose' in student):
#     print('Rose 在集合中')
# else:
#     print('Rose 不在集合中')
#
# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
#
# print(a)
#
# print(a - b)  # a和b的差集
#
# print(a | b)  # 3917804740
#
# print(a & b)  # a和b的交集
#
# print(a ^ b)  # a和b中不同时存在的元素

##集合（set）是一个无序不重复元素的序列。
##可以使用大括号 { } 或者 set() 函数创建集合

# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
#
# tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
#
# print(dict['one'])  # 输出键为 'one' 的值
# print(dict[2])  # 输出键为 2 的值
# print(tinydict)  # 输出完整的字典
# print(tinydict.keys())  # 输出所有键
# print(tinydict.values())  # 输出所有值

# print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]))
#
# print({x: x**2 for x in (2, 4, 6)})
#
# print(dict(Runoob=1, Google=2, Taobao=3))

##2018-4-19

# a = "Hello"
# b = "Python"
#
# print("a + b 输出结果：", a + b)
# print("a * 2 输出结果：", a * 2)
# print("a[1] 输出结果：", a[1])
# print("a[1:4] 输出结果：", a[1:4])
#
# if ("H" in a):
#     print("H 在变量 a 中")
# else:
#     print("H 不在变量 a 中")
#
# if ("M" not in a):
#     print("M 不在变量 a 中")
# else:
#     print("M 在变量 a 中")
#
# print(r'\n')
# print(R'\n')

