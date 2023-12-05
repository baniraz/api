# for a in range(2, 8):
#     print(a * '*')
from math import *

import pytest

# a, d, f = input(), '', '4'
# b = input('vvedeno')
# c = input()
# print('vvedeno', name)
# print(name, '- 4empion')
# print('name1', 'n2', end='\n\n')
# a = int(input())
# v = a**3
# s = 6*a**2
# # b = int(input())
# print(f'test = {s}', a, sep='\n')
# a = max(1, 3.8, 3)
# n1 = -2
# n2 = 0.4
# print(-n1+5)
# print(ceil(n2))

# for i in range(5, 5):
#     print('f')
# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')
# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
#     print(a)

# num = int(input())
# has_seven = False  # сигнальная метка
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
#
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')
# n=int(input())
# flag = True
# for i in range(2, n):
#     if n % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#         print(n)
#
# for j in range(7 + 1):
#     print('*', end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# for x in range(0, 100):
#     for y in range(0, 100):
#         for m in range(0, 100):
#             if (10 * x + 5 * y + 0.5 * m == 100) and (x + y + m == 100):
#                 print('x =', x, 'y =', y, m)
# print('Общее количество натуральных решений =',)

# s = 'abcdef'
# for i in range(len(s)):
#     print(s[i])
#
# s = 'abcdef'
# for c in s:
#     print(c)
# s = 'abcdefg'
# print(s[::-3])
# print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)
# s = 'www.stepik.org'
# print(s.startswith('www'))
# s = 'I learn Python language. Python - awesome!'
# print(s.find('Python'))
# s = 'abcdababa'
# print(s.replace('ab', '123'))
# fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
# fruits[2:5] = []
#

# names = []  # создаем пустой список
# #
# # numbers.append(100)
# # numbers.extend([1])
# # print(numbers)
# names[0] = 'Chromatica'
# print(names)
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in range(len(numbers)):
#     print(numbers[i])
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for num in numbers:
#     print(num, end=' ')

# numbers = input().split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# print(numbers)
# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
# # for i in range(len(food)):
# #     while i in
# while 'Рис' in food:
#     food.remove('Рис')
# print(food)
# original_list = [1, 2, 4, 7]
# modified_list = original_list.append(666)  # тут ничего не возвращается
#
# print(original_list)  # [1, 2, 4, 7, 666]
# print(modified_list)
# chars = [c for c in 'abcdefg']
# # print(chars)
# n = int(input())
# lines = [input() for _ in range(n)]
# print(lines)
# numbers = [i+j for i in range(1, 5) for j in range(2)]
# print(numbers)
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
#
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
#             a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами
#
# print('Отсортированный список:', a)
# def draw_box():
#     for _ in range(5):
#         print('*' * 7)
#
# draw_box()
# print()\
# x = 4
#
# def add():
#     global x
#     x = 3
#     x = x + 5
#     print(x)
#
# add()
# print(x)
# def get_sum(x, y, z):
#     return x + y + z
#     print('Сумма равна', x + y + z)
#
# print(get_sum(1, 2, 3))
# def is_invalid(model):
#     if model != 100 and model != 200 and model != 300:
#         return True
#     else:
#         return False
#
# model = int(input())
# while is_invalid(model):
#     print('Допустимыми номерами моделей являются 100, 200 и 300.')
#     model = int(input())
# import random
#
# random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
#
# for _ in range(10):
#     print(random.randint(1, 100))
# numbers = [5, 10, 15, 25]
# print(numbers[::-2])

# numbers = [10, 20, 30, 40, 50]
# numbers.pop()
# print(numbers)
#
# numbers.pop(2)
# print(numbers)
#
# words = ['xyz', 'zara', 'beegeek']
# print(max(words))
# num=[1,2,3,4,5,6,7,8,9,0]
# count=['one','two','three','four','five','six','seven','eight','nine','zero']
#
# mas=dict(zip(num,count))
# print(mas)
# d={'CS101': {'audience_number': '3004', 'teacher': 'Хайнс', 'time': '8:00'},
# 'CS102': {'audience_number': '4501', 'teacher': 'Альварадо', 'time': '9:00'},
# 'CS103': {'audience_number': '6755', 'teacher': 'Рич', 'time': '10:00'},
# 'NT110': {'audience_number': '1244', 'teacher': 'Берк', 'time': '11:00'},
# 'CM241': {'audience_number': '1411', 'teacher': 'Ли', 'time': '13:00'}}
# n=input()
# li=[]
# di={}
# for k in d:
#     if k==n:
#         for value in d[k].values():
#             li.append(value)
#         di[k]=li
# print(di)
#
# silka = input()
# a = silka.find('clickid') + 8
# print(silka[a])
# print(a)
#
# b = len(silka)
# print(b)
#
# c = silka.find('&', a, b)
# print(c)
#
# if c != -1:
#     print(silka[a:c])
# else:
#     print(silka[a:b])

# def test1():
#     li=[]
#     for i in range(30):
#         if i!=0:
#             if i%3==0:
#                 # print('fuz')
#                 li.append('fuz')
#             elif i%5==0:
#                 li.append('buz')
#             elif i%3==0 and i%5==0:
#                 li.append('fuzbuz')
#             else:
#                 li.append(i)
#         else:
#             li.append(i)
#     print(li)

# f = 'hghgjTghgh'
# e = 'GgjgY'
# t = 'jhjjjhj'
#
# # @pytest.mark.parametrize('s', [f, e, t])
# def ex(s):
#     for i in s:
#         if i == i.upper():
#             a = 'da'
#         else:
#             a = 'net'
#     if a == 'da':
#         print(True)
#     if a == 'net':
#         print(False)







