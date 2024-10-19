# rg = range(10,50,5)
# for i in rg:
#     print(i)
from itertools import count

# Type conversion
# x = 10
# y = float(x)
# print(y,type(y))

# r = range(1, 100, 6)
# for each in r:
#     print(each)


# x = 24
# y = 20
#
# lst = [10, 20, 30, 40, 50]
#
# if x not in lst:
#     print("x is NOT present in given list")
# else:
#     print("x is present in given list")
#
# if y in lst:
#     print("y is present in given list")
# else:
#     print("y is NOT present in given list")
#

# x = 24
# y = 20
# ls = [10, 20, 30, 40, 50]
#
# if x in ls:
#     print("x is present")
# else:
#     print("x is not present")
#
# if y in ls:
#     print("y is present")
# else:
#     print("y is not present")

# sum of even numbers

#sum of even numbers 10--0+2+4+6+8=20

# total = int(input("Enter a number: "))
# res = 0
# for each in range(1, total):
#     if each % 2 == 0:
#         res += each
# print("sum of even: ", res)

# 19 Implement a program to reverse a string without using built-in functions.

# text = input("Enter a word/sentence: ")
# reverse_string = ""
# for each in range(len(text)-1,-1,-1):
#     reverse_string += text[each]
# print("original string is: ", text)
# print("Reverse of a string is: ", reverse_string)

# text = input("Enter a word/sentence: ")
# rev = ""
# for each in text:
#     rev = each+rev
# print(rev)

# find the first occurrence of a number

# lst = [12, 10, 35, 10, 10, 14,15,18,14, 28]
# num = int(input("enter a number from a list: "))
# count = 0
# while count < len(lst):
#     if lst[count] == num:
#         break
#     count += 1
# else:
#     count = 0
# print(count)

#fact

# fact = int(input("enter a number: "))
# res = 1
# while fact > 1:
#     res *= fact
#     fact -= 1
# print(res)


# Both setdefault() and get() are methods in Python dictionaries used to handle missing keys, but they work in slightly different ways:
# get(key, default)
# Returns the value associated with the key if the key exists in the dictionary.
# If the key is not found, it returns the default value provided as the second argument. If no default is specified, it returns None.
# Does not modify the dictionary.
# Example:
# Python
#
#
#
# Execution output
# my_dict = {'a': 1, 'b': 2}
#
# print(my_dict.get('a', 0))
# print(my_dict.get('c', 0))
# print(my_dict)
# 1
# 0
# {'a': 1, 'b': 2}
# setdefault(key, default)
# Returns the value associated with the key if the key exists in the dictionary.
# If the key is not found, it creates a new entry in the dictionary with the key and sets its value to the default provided.
# If no default is specified, it sets the value to None.
# Modifies the dictionary if the key does not exist.
# Example:
# Python
#
#
#
# Execution output
# my_dict = {'a': 1, 'b': 2}
#
# print(my_dict.setdefault('a', 0))
# print(my_dict.setdefault('c', 0))
# print(my_dict)


# dt = {"name": "Ramesh", "age":25, "salary": 2500, "is_perm": True, "location":"Bangalore"}
# rs = dt.setdefault("bonus",1000)
# print(rs)
# print(dt)


# imp in real time
# string to dict by taking each char as key and setting default values for each char...

# st = "python"
# dc = {}
# n = 0
# for each in st:
#     if each in st:
#         dc.setdefault(each, n)
#         n += 1
# print(dc)

# st1 = "python_developer"
# dc1 = {}
# for each in st1:
#     dc1.setdefault(each, 100)
# print(dc1)


# get the total occurrences as th values by taking key name from a string....
#
# st2 = "python_is_python"
# dc2 = {}
# for each in st2:
#     if each in dc2:
#         dc2[each] += 1
#     else:
#         dc2[each] = 1
# print(dc2)

# st3 = "Bengaluru_is"
# dc3 = {}
# for each in st3:
#     dc3.setdefault(each, "amazing")
# print(dc3)

# number of occurrences

# st4 = "bengaluru_is_amazing"
# dc4 = {}
# for each in st4:
#     if each in dc4:
#         dc4[each] += 1
#     else:
#         dc4[each] = 1
# print(dc4)

# find the number is power of 2 and power of 3

# power of 2
# using for loop

# num = int(input("enter a number: "))
# for each in range(num):
#     if num % 2 != 0:
#         print("no")
#         break
#     if num == 2**each:
#         print("yes")
#         break
#     if num <= 2**each:
#         print("no")
#         break
# else:
#     print("no")

# power of 2
# using while loop

# num = int(input("enter a number: "))
# step = 0
# while num >= 2**step:
#     if num%2 != 0:
#         print("no")
#         break
#     if num == 2**step:
#         print("yes")
#         break
#     step += 1
# else:
#     print("no")


# cont = 2
# lst = []
# while cont < 50:
#     lst.append(cont)
#     cont += 2
# print(lst)

# prime number
# num = int(input("enter a number: "))
# if num > 1:
#     for each in range(2,num):
#         if num % each == 0:
#             print("it is not a prime")
#             break
#     else:
#         print("it is a prime")
# else:
#     print("it is not a prime")

# perfect number
# 124 = sum of all divisors = 124

# num = int(input("enter a number: "))
# res = 0
# for each in range(1, num):
#     if num % each == 0:
#         res += each
#         if res == num:
#             print(res, "is a perfect number")
#             break
# else:
#     print("not a perfect number")

# power of 2 or 3

# num = int(input("enter a number: "))
#
# if num > 1:
#     for each in range(num):
#         if num == 2**each:
#             print("it is a power of 2")
#             break
#     else:
#         print("no")
# else:
#     print("no")


# number is strong or not
#
# num = int(input("enter a number: "))
# tot = 0
# temp = num
# while temp:
#     rem = num % 10
#     x = 1
#     facto = 1
#     while x <= rem:
#         facto *= x
#         x += 1
#     tot += facto
#     temp //= 10
# if tot == num:
#     print("yes")
# else:
#     print("no")

# armstrong number

# num = int(input("enter a number: "))
# tot = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     tot += digit**3
#     temp //= 10
# if tot == num:
#     print("yes")
# else:
#     print("no")

# reverse of a string

# st = "python"
# st1 = ""
# for each in st:
#     st1 = each+st1
# print(st1)

# reverse of a number

# num = int(input("enter a number: "))
# res = 0
# for each in str(num):
#     digit = num % 10
#     res = res*10+digit
#     num //= 10
# print(res)

# ls = [('name', 'Ramesh'), ('age', 25), ('salary', 2500), ('is_perm', True), ('location', 'Bangalore')]
# y = dict(ls)
# print(y)
# ls1 = ["a", "b", "c","d","e"]
# ls2 = [11, 22, 33]
# z = zip(ls1, ls2)
# y = dict(z)
# print(y)
# x = y.setdefault("d", 44)
# print(x)

# print(dir(set))
# to remove duplicates from list using set

# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# new = list(set(test_list))
# print(new)


# using list comprehension to remove duplicated from list

# test_list = [1, 3, 5, 6, 3, 5, 6, 1]
# lst = []
# [lst.append(each) for each in test_list if each not in lst]
# print(lst)
#
# res = []
# [res.append(x) for x in test_list if x not in res]


# --- star pattern---
# n = 5
# for i in range(n):
#     for j in range(n+i):
#         if i+j >= n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = 5
# for i in range(n):
#     for j in range(n+0):
#         if i+j >= n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# pyramid pattern printing
# n = int(input("enter a number: "))
# n1 = 1
# for i in range(1,n*2):
#     if i%2 != 0:
#         print("  "*(n-n1)+ "* " * i)
#         n1 += 1


#   map,reduce,filter in lambda functions

# sum all the numbers in a list

# from functools import reduce
# #
# # reduce to get cumulative sequence type
#
# ls = [58, 555, 879, 666, 475, 369]
#
# addition = reduce((lambda x, y: x+y), ls)
#
# print(addition)


# mapping

# from functools import reduce
#
# ls = [2, 4, 5, 8]
#
# multi = list(map((lambda x: x * 2), ls))
# print(multi)

# filter

# ls = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#
# odd = list(filter(lambda x: (x % 2 == 0), ls))
# print(odd)

# ls = ["python", "world", "bengaluru", "kolar"]
# # length = map((lambda x: len(x)), ls)
# length = map((lambda x: len(x)),ls)
# print(list(length))


# --number of words without using split o/p 3
#
# st = "python is world"
# word = 1
# for each in st:
#     if each == ' ':
#         word = word+1
# print(word)

# st = "python is world of programming"
#
#
# def word(st1):
#     w = 1
#     for each in st:
#         if each == ' ':
#             w += 1
#     return w
#
#
# res = word(st)
# print(res)

# --find the max and 2nd max element in a list

# ls = [58, 555, 879, 666, 475, 369]
#
#
# def maxi(ele):
#     max_ele = ls[0]
#     for each in ls:
#         if each > max_ele:
#             max_ele = each
#     return max_ele
#
#
# res = maxi(ls)
# print(res)

# ls = [58, 555, 879, 666, 475, 369]
#
# ls1 = set(ls)
# ls1.remove(max(ls1))
# print(max(ls1))


# num = 5
# for i in range(num):
#     for j in range(num-i):
# print()
# print('*',end=' ')

# n = 'i love you '
# while n > 'i hate you':
#     print(n)

# age = 32


# The test condition is always True
# while age > 18:
#     print('You can vote')
#     break

# while True:
#     name = input("enter your name: ")
#     if name == "manu":
#         print(name)
#         break
#     else:
#         print("incorrect")

# Program to print odd numbers from 1 to 100

# num = 0
#
# while num < 100:
#     num += 1
#
#     if (num % 2) == 0:
#         continue

# print(num)


# Write a function to calculate the sum of elements in a list that are greater than a given number.
#
# Return the sum of the numbers greater than the given number.
# If numbers is [1, 2, 3, 4, 5] and n is 3, the return value should be 9 because 4 + 5 is 9.

# def sum_greater(numbers, n):
#     numbers = [1, 2, 3, 4, 5]
#     n = 3
#     res = 0
#     for each in numbers:
#         if each > 3:
#             res = res + each
#         continue
#     return res
#
#
# print(sum_greater([1, 2, 3, 4, 5], 3))

# using index position

# numbers = [1, 2, 3, 4, 5]
# n = 2
# res = 0
# for each in numbers:
#     if each > numbers[n]:
#         res += each
#     continue
# print(res)

# Program to count the number of each vowels

# string of vowels
# vowels = 'aeiou'
#
# ip_str = 'Hello, have you tried our tutorial section yet?'
#
# # make it suitable for caseless comparisions
# ip_str = ip_str.casefold()
#
# # make a dictionary with each vowel a key and value 0
# count = {}.fromkeys(vowels,0)
#
# # count the vowels
# for char in ip_str:
#    if char in count:
#        count[char] += 1
#
# print(count)

# ip_str = 'Hello, have you tried our tutorial section yet?'
# vowels = "aeiou"
# ip_str = ip_str.casefold()
# dc = {}.fromkeys(vowels,0)
# for each in ip_str:
#     if each in dc:
#         count[each] += 1
# print(dc)

# Python List Methods
# Python has many useful list methods that make it really easy to work with lists.
#
# Method	Description
# append()	Adds an item to the end of the list
# extend()	Adds items of lists and other iterables to the end of the list
# insert()	Inserts an item at the specified index
# remove()	Removes the specified value from the list
# pop()	Returns and removes item present at the given index
# clear()	Removes all items from the list
# index()	Returns the index of the first matched item
# count()	Returns the count of the specified item in the list
# sort()	Sorts the list in ascending/descending order
# reverse()	Reverses the item of the list
# copy()	Returns the shallow copy of the list

# Write a function to find the largest number in a list.
#
# For input [1, 2, 9, 4, 5], the return value should be 9.


# def max_in_list(ls):
#     ls = [1, 2, 9, 4, 5]
#     max_num = 0
#     for each in ls:
#         if each > max_num:
#             max_num = each
#     return max_num
#
#
# print(max_in_list([1, 2, 9, 4, 5]))

# ls = [1, 2, 9, 9, 5]
# max_num = 0
# min_num = 0
# for each in ls:
#     if each > max_num:
#         max_num = each
#     if each < min_num:
#         min_num = each
# print(max_num)
# print(min_num)


# Methods of Python String
# Besides those mentioned above, there are various string methods present in Python. Here are some of those methods:
#
# Methods	Description
# upper() 	Converts the string to uppercase
# lower()	Converts the string to lowercase
# partition()	Returns a tuple
# replace()	Replaces substring inside
# find()	Returns the index of the first occurrence of substring
# rstrip()	Removes trailing characters
# split()	Splits string from left
# startswith()	Checks if string starts with the specified string
# isnumeric()	Checks numeric characters
# index()	Returns index of substring

# def outer(x):
#     def inner(y):
#         return x + y
#
#     return inner


# add_five = outer(5)
# result = add_five(6)
# print(result)

# func as argument

# def add(x, y):
#     return x + y
#
#
# def calculate(func, x, y):
#     return func(x, y)
#
#
# res = calculate(add,7,3)
# print(res)

# Return a Function as a Value

# def greeting(name):
#     def hello():
#         return "Hello, " + name + "!"
#
#     return hello


# greet = greeting("Atlantis")
# print(greet())


# def make_pretty(func):
#     # define the inner function
#     def inner():
#         # add some additional behavior to decorated function
#         print("I got decorated")
#
#         # call original function
#         func()
#
#     # return the inner function
#     return inner


# define ordinary function
# def ordinary():
#     print("I am ordinary")
#
#
# # decorate the ordinary function
# decorated_func = make_pretty(ordinary)
#
# # call the decorated function
# decorated_func()


# @ decorator example

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return
#
#         return func(a, b)
#
#     return inner
#
#
# @smart_divide
# def divide(a, b):
#     print(a/b)
#
# divide(6,5)

#  example 2

# def multi_dec(func):
#     def inner(a, b):
#         print("i am going to multiply", a, "and", b)
#         return func(a, b)
#
#     return inner
#
#
# @multi_dec
# def multiplication(a,b):
#     print(a * b)
#
#
# multiplication(5, 6)

# chaining of decorators

# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 15)
#         func(*args, **kwargs)
#         # print("*" * 15)
#
#     return inner
#
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 15)
#         func(*args, **kwargs)
#         # print("%" * 15)
#
#     return inner
#
#
# @star
# @percent
# def printer(msg):
#     print(msg)
#
#
# printer("Hello")


# def symbol(func):
#     def wrapper(*args, **kwargs):
#         print("$" * 10)
#         func(*args, **kwargs)
#
#     return wrapper
#
#
# def ash(func):
#     def wrapper(*args, **kwargs):
#         print("#" * 10)
#         func(*args, **kwargs)
#
#     return wrapper
#
#
# @symbol
# @ash
# def original(a, b,c):
#     print(a*b*c)


# original(5, 6,8)

# import re
#
# string = 'hello 12 hi 89. Howdy 34'
# pattern = "\d+"
#
# result = re.findall(pattern, string)
# print(result)

# convert binary value to decimal

# bina = input("enter a binary value: ")
# decimal = 0
# for each in bina:
#     decimal = decimal * 2 + int(each)
# print(decimal)

# convert decimal to binary
# def decToBin(n):
#     if n == 0:
#         return ''
#     else:
#         return decToBin(n // 2) + str(n % 2)
#
# print(decToBin(17))


# def dec_bin(n):
#     if n == 0:
#         return ""
#     else:
#         return dec_bin(n // 2) + str(n%2)
#
# print(dec_bin(17))

# sum of n positive integers
#
# n = int(input("enter a number: "))
# res = 0
# for each in range(1,n+1):
#     res += each
# print(res)


# Prompt the user to input a four-digit number and convert it to an integer.
# num = int(input("Input a four-digit number: "))
#
# # Extract the thousands digit (x).
# x = num // 1000
# print(x)
#
# # Extract the hundreds digit (x1) by subtracting the thousands digit from the number.
# x1 = (num - x * 1000) // 100
# print(x1)
#
# # Extract the tens digit (x2) by subtracting the thousands and hundreds digits from the number.
# x2 = (num - x * 1000 - x1 * 100) // 10
# print(x2)
#
# # Extract the ones digit (x3) by subtracting the thousands, hundreds, and tens digits from the number.
# x3 = num - x * 1000 - x1 * 100 - x2 * 10
# print(x3)
#
# print(x+x1+x2+x3)

# n = int(input("enter a 4 digit number: "))
#
# x = n // 1000
# x1 = (n-x*1000) // 100
# x2 = (n-x*1000-x1*100) // 10
# x3 = n-x*1000-x1*100-x2*10
# res = x+x1+x2+x3
# print(x)
# print(x1)
# print(x2)
# print(x3)=
# print(res)

# s = "The quick brown fox jumps over the lazy dog."
# cont = 0
# # print(s.count("o"))
# for each in s:
#     if each == "o":
#         cont += 1
#
# print(cont)

# for i in range(5):
#     print("from i", i,end="")
#
#     for j in range(i + 1):
#         print("from j",j)
#         # print("* ", end="")
#     # print()

# print pattern of star\\


# for i in range(5):
#     for j in range(i + 1):
#         print("* ", end="")
#     print()


# res = 0
# for each in range(1, 101):
#     res += each
# print(res)

# Calculate the sum of numbers from 1 to 100 using a while loop:

# num = 1
# sum_numbers = 0
# while num <= 100:
#     sum_numbers += num
#     num += 1
# print(sum_numbers)


# prime numbers between 1-50

# for num in range(2, 51):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)

# Print numbers divisible by 3 or 5 from 1 to 20 using a for loop:

# for each in range(1,21):
#     if each % 3 == 0 or each % 5 == 0:
#         print(each)

# Print a list of squares of numbers from 1 to 5 using a list comprehension:

# sq = [each**2 for each in range(1,6)]
# print(sq)

# Print the Fibonacci sequence up to the 10th term using a while loop:
# a, b = 0, 1
# cnt = 0
# while cnt < 10:
#     print(a, end=" ")
#     a, b = b, a + b
#     cnt += 1

# using for loop
# a,b = 0,1
# for each in range(10):
#     print(a, end=" ")
#     a,b = b, a+b


# for num in range(1, 11):
#     if num % 2 == 0:
#         continue
#     print(num)
# else:
#     print("Loop completed successfully!")

# print only positive values

# nums = [34, 1, 0, -23, 12, -88]
# new_nums = list(filter(lambda x: x > 0, nums))
# print(new_nums)

# nums = [34, 1, 0, -23, 12, -88]
# new_nums = []
# for each in nums:
#     if each > 0:
#         new_nums.append(each)
# print(new_nums)

# Python: Count number of items in a dictionary value that is a list

# dt = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

# cnt = sum(map(len, dt.values()))
# print(cnt)


# -- FIBONACCI SERIES upto 10th number--

# a, b = 0, 1
# cnt = 0
# while cnt < 10:
#     print(a, end=" ")
#     a,b = b, a+b
#     cnt += 1


# def fibo(n):
#     a, b = 0, 1
#     for each in range(10):
#         print(a, end=" ")
#         a, b = b, a + b
#
#
# fibo(10)


# --factorial
# fact = int(input("enter a number: "))
# res =1
# while fact > 1:
#     res *= fact
#     fact -= 1
# print(res)
#
# res = 1
# for each in range(fact):
#     res *= fact
#     fact -= 1
# print(res)

# email validation

# import re
#
#
# # Define a function for
# # for validating an Email
# def check(s):
#     pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#     if re.match(pat, s):
#         print("Valid Email")
#     else:
#         print("Invalid Email")
#
#
# # Driver Code
# if __name__ == '__main__':
#     # Enter the email
#     email = "ankitrai326@gmail.com"
#
#     # calling run function
#     check(email)
#
#     email = "my.ownsite@our-earth.org"
#     check(email)
#
#     email = "ankitrai326.com"
#     check(email)


# check for mobile numbers

#
#     # 1) Begins with  +91
#     # 2) Then contains 6,7 or 8 or 9.
#     # 3) Then contains 9 digits


# import re
#
# design = r'^(\+91-[6-9]{1}\d{9})'
#
# phone_pattern = re.compile(design)
#
# phone_number = "+91-5925635896"
# k = phone_pattern.match(phone_number)
# print(k)
# if phone_pattern.match(phone_number):
#     print("Valid phone number")
# else:
#     print("Invalid phone number")
# r'^(\+91-[6-9]{1}\d{9})'
# r'\+{1}91-[6-9]{1}\d{9}'
#
# import re
#
# design_pattern = r'\+{1}91-[6-9]{1}\d{9}'
#
# pattern_compile = re.compile(design_pattern)
#
# phone_number = "+91-9956894565"
# k = pattern_compile.fullmatch(phone_number)
#
# print(k)
#
# if pattern_compile.fullmatch(phone_number):
#     print("valid phone number")
# else:
#     print("invalid phone number")


# mail pattern
# pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'


# Explanation of the Simple Regex Pattern:
# ^ asserts the start of the string.
# [\w\.-]+ matches one or more word characters (letters, digits, and underscores), dots, or hyphens.
# @ matches the "@" symbol.
# [\w\.-]+ matches the domain name part (letters, digits, dots, and hyphens).
# \. matches a literal dot.
# \w+ matches one or more word characters for the top-level domain.
# $ asserts the end of the string.

# ls = ["flower","flight","flow"]
# ---inheritance oop's'

# class Animal:
#     def __init__(self, animal):
#         print(animal, "is an animal")
#
#
# class Mammal(Animal):
#     def __init__(self, mammalname):
#         print(mammalname, "is a warm-blooded animal")
#         super().__init__(mammalname)
#
#
# class NonWingedAnimal(Mammal):
#     def __init__(self, nonwingedanimal):
#         print(nonwingedanimal, "can't fly")
#         super().__init__(nonwingedanimal)
#
#
# class NonMarineAnimal(Mammal):
#     def __init__(self, nonmarineanimal):
#         print(nonmarineanimal, "can't swim")
#         super().__init__(nonmarineanimal)
#
#
# class Dog(NonWingedAnimal, NonMarineAnimal):
#     def __init__(self,name):
#         print(name, "has 4 legs")
#         super().__init__(name)
#
#
# a = Dog('Labrador')


# class Animal:
#     def __init__(self, animal):
#         self.animal = animal
#         print(animal, "is an animal")
#
#
# class Mammal(Animal):
#     def __init__(self, mammalname):
#         self.mammalname = mammalname
#         print(mammalname, "is a warm-blooded animal")
#         super().__init__(mammalname)
#
# class NonWingedAnimal(Mammal):
#     def __init__(self,nonwingedanimal):
#         self.nonwingedanimal = nonwingedanimal
#         print(nonwingedanimal, "can't fly")
#         super().__init__(nonwingedanimal)
#
# class NonMarineAnimal(Mammal):
#     def __init__(self,nonmarineanimal):
#         self.nonmarineanimal=nonmarineanimal
#         print(nonmarineanimal, "can't swim")
#         super().__init__(nonmarineanimal)
#
#
# class Dog(NonMarineAnimal,NonWingedAnimal):
#     def __init__(self):
#         print("Dog has 4 legs")
#         super().__init__("dog")


# d = Dog()
# b = NonMarineAnimal('Bat')
# c = NonWingedAnimal('Dog')
# e = Mammal('cow')
# f = Animal('Rabbit')

# --generators

# def gen_range(start, stop):
#     while start < stop:
#         yield start
#         start += 1
#
#
# x = gen_range(2, 7)
# # print(next(x))
# # print(next(x))
# for each in x:
#     print(each)

# ls = ["flower", "flight", "flow"]
#
# for each in ls:
#     if each[:2] == "fl":
#         com = each[:2]
# print(com)

# find the count of spaces
# str1 = "python is fun "
# cnt = 0
# for each in str1:
#     if each.isspace():
#         cnt += 1
# print(cnt)

# str1 = "python is fun "
# cnt = 0
# for each in str1:
#     if each == " ":
#         cnt += 1
# print(cnt)


# find the most frequent char in a string
# str1 = "banana"
# cnt = 0
# st = set(str1)
# dt = {}
# for each in str1:
#     if each in st:
#         dt[each] =
#         cnt += 1
# print(dt)

# res = max(str1,key=lambda x: str1.count(x))
# print(res)


# find the common keys in 2 dicts o/p = ['b']
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
#
# st1 = set(dict1)
# st2 = set(dict2)
#
# res = st1.intersection(st2)
# print(list(res))

# for each in dict1:
#     if each in dict2:
#         print(list(each))

# remove keys from dict that has specific value
# key = 1 o/p {'b': 2}
# dt = {'a': 1, 'b': 2, 'c': 1}
# dt2 = {}
#
# for key,value in dt.items():
#     if value != 1:
#         dt2[key] = value
# print(dt2)

# intersection of two sets o/p {2,3}
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
#
# res = set1.intersection(set2)
# print(res)

# find the longest string
# lst = ["data","science","world","python","world_is_beautiful"]
# length = [len(x) for x in lst]
# ind = length.index(max(length))
# # print(length)
# print(lst[ind])


# create a dictionary using string by giving some default and
# s = "python is python"
# dc = {}
# for each in s:
#     dc[each] = 100
# print(dc)

# or

# for each in s:
#     dc.setdefault(each,100)
# print(dc)

# then by occurrence as values and
# s = "python is a programming language"
# dc = {}
# for each in s:
#     if each in dc:
#         dc[each] += 1
#     else:
#         dc[each] = 1
# print(dc


# then n*n as value for range of n

# num = int(input("enter a number: "))
# dc ={}
# for key in range(num):
#     dc[key] = key*key
# print(dc)

# for key in range(num):
#     dc.setdefault(key,key*key)
# print(dc)

# number is armstrong or not

# num = int(input("enter a number: "))
#
# tot = 0
# temp = num
# power = str(num)
# p = len(power)
# while temp > 0:
#     digit = temp % 10
#     tot += digit**p
#     temp //= 10
# if tot == num:
#     print("it is an armstrong number")
# else:
#     print("Not an armstrong number")

# anagram

# s1 = input("enter a string: ")
# s2 = input("enter a string: ")
#
# if len(s1) == len(s2):
#     for each in s1:
#         if each not in s2:
#             print("not an anagram")
#             break
#     print("anagram")
# else:
#     print("not an anagram")

# word is palindrome or not
#
# word = input("enter a word: ")
#
# if word == word[::-1]:
#     print("it is a palindrome")
# else:
#     print("not a palindrome")

# exception handling


# try:
#     x = 10 / 0
#     print(x)
#     print(name)
#     ls = [1,4,8,4]
#     print(ls[4])
#     dc = {"name": "john", "age": 25}
#     v = dc['sal']
#     print(v)
# except KeyError as ke:
#     print(f"Key error: {ke}")
# except IndexError as ie:
#     print(f"Index error: {ie}")
# except NameError as ne:
#     print(f"Name error: {ne}")
# except ZeroDivisionError as zde:
#     print(f"Zero div error: {zde}")
# else:
#     new_sal = v*5
#     dc['sal'] = new_sal
#     print(dc)


# program for handling errors like zerodivision error,value error, key error,index error, type error
#     and type error with syntax
# try:
#     a = 2 + "3"
#     b = int("hello")
#     c = 10/0
#     print(name)
#     ls = [1,4,8,4]
#     print(ls[4])
#     dc = {"name": "john", "age": 25}
#     v = dc['sal']
#     print(v)
# except (NameError,KeyError,ValueError,IndexError,TypeError,ZeroDivisionError) as error:
#     print(f"from except: {error}")


# prime number upto n using list comprehension
# num = 50
# pr = [n for n in range(2,num) if all(n % each != 0 for each in range(2,n))]
# print(pr)

#
# number = int(input("enter the number: "))
# #
# for n in range(2, number + 1):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n)

# def prime(n):
#     res = [n for n in range(2, n) if all(n % each != 0 for each in range(2, n))]
#     return res
#
#
# print(prime(50))

# def bubbleSort(nlist):
#     for passnum in range(len(nlist) - 1, 0, -1):
#         for i in range(passnum):
#             if nlist[i] > nlist[i + 1]:
#                 temp = nlist[i]
#                 nlist[i] = nlist[i + 1]
#                 nlist[i + 1] = temp


# nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]


# bubbleSort(nlist)
# print(nlist)

# s = "pYthoN iS PythoN"
# cntl = 0
# cntu = 0
#
# for each in s:
#     if each.islower():
#         cntl += 1
#     if each.isupper():
#         cntu += 1
# print(f"{cntl: }\n{cntu: }")

# lower = "abcdefghijklmnopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# for each in s:
#     if each in lower:
#         cntl += 1
#     if each in upper:
#         cntu += 1
# print(cntl,cntu)

# maximum of 4 numbers

# num1 = int(input("enter a number1: "))
# num2 = int(input("enter a number2: "))
# num3 = int(input("enter a number3: "))
# num4 = int(input("enter a number4: "))
#
# ls = [num1,num2,num3,num4]
# maxi = ls[0]
# for each in ls:
#     if each > maxi:
#         maxi = each
# print(maxi)

# find the highest length of the string and index number using one for loop

# list1=['ramnetha','dreams','apple', 'software','developers']
# k=sorted(list1,key=len)
# print(k)
# length=len(list1[-1])
# j=list1[-1]
# index=0
# for i in range(len(list1)):
#     if list1[i]==j:
#         index=i
#         print(length,index)

# phone = r'\+{1}91-[6-9]{1}\d{9}'
# mail = r'^[\w\.-]{1,8}+@[\w\.-]{1,7}+\.\w{2,3}+$
# pattern = r"^\w{1,9}@\w{1,8}\.\w{2,3}$"
# r"^\w{1,9}@[\gmail|email]\.\w{2,3}$"
# Write a program that extracts different components
# (protocol, domain, path, etc.) from a given URL using regular expressions.

#
# import re
#
#
# def extract_url_components(url):
#     # Regular expression to extract components from a URL
#     pattern = r'^(?P<protocol>https?|ftp)://(?P<domain>[^/:]+)(?P<port>:\d+)?(?P<path>/[^?#]*)?(?P<query>\?[^#]*)?(?P<fragment>#.*)?$'
#
#     match = re.match(pattern, url)

#     if match:
#         components = match.groupdict()
#         return components
#     else:
#         return None
#
#
# # Example usage
# url = "https://www.example.com:8080/path/to/page?name=example&value=test#section"
# components = extract_url_components(url)
#
# if components:
#     print("URL Components:")
#     for key, value in components.items():
#         print(f"{key}: {value}")
# else:
#     print("Invalid URL")


# Explanation:
# protocol: Matches the scheme of the URL (http, https, ftp, etc.).
# domain: Captures the domain name (e.g., www.example.com).
# port: Matches an optional port (e.g., :8080).
# path: Captures the path after the domain (e.g., /path/to/page).
# query: Matches an optional query string (e.g., ?name=example&value=test).
# fragment: Captures an optional fragment (e.g., #section).
# This program will correctly parse the components of a URL and return them as a dictionary.

# with open('example.txt', 'r') as file:
#     data = file.read()
#     print(data)

# with open('example.txt','w') as file:
#     file.write("hey hi")
#     data = file.read()
#     print(data)
#
# 1. r (Read Mode)
# Purpose: Opens a file for reading.
# Behavior:
# If the file exists, it opens the file for reading.
# If the file does not exist, it raises a FileNotFoundError.
# You can read the file using methods like .read(), .readline(), or .readlines().
# The file pointer: Positioned at the beginning of the file.
# Example:
# python
# Copy code
# file = open("example.txt", "r")
# content = file.read()
# file.close()
#
# 2. r+ (Read and Write Mode)
# Purpose: Opens a file for both reading and writing.
# Behavior:
# If the file exists, it opens the file for reading and writing.
# If the file does not exist, it raises a FileNotFoundError.
# Allows both reading and writing within the file.
# The file pointer: Positioned at the beginning of the file.
# Does not truncate the file (i.e., it does not delete the contents).
# Example:
# python
# Copy code
# file = open("example.txt", "r+")
# content = file.read()  # Read the content
# file.write("New Data")  # Write new data
# file.close()
#
# 3. w (Write Mode)
# Purpose: Opens a file for writing.
# Behavior:
# If the file exists, it truncates the file to zero length (i.e., deletes the content).
# If the file does not exist, it creates a new file.
# You can only write to the file, reading is not allowed.
# The file pointer: Positioned at the beginning of the file.
# Example:
# python
# Copy code
# file = open("example.txt", "w")
# file.write("Writing new data")
# file.close()
#
# 4. w+ (Write and Read Mode)
# Purpose: Opens a file for both writing and reading.
# Behavior:
# If the file exists, it truncates the file to zero length (i.e., deletes the content).
# If the file does not exist, it creates a new file.
# Allows both reading and writing.
# The file pointer: Positioned at the beginning of the file.
# Example:
# python
# Copy code
# file = open("example.txt", "w+")
# file.write("Writing data")
# file.seek(0)  # Move pointer to the beginning for reading
# content = file.read()
# file.close()
#
# 5. a (Append Mode)
# Purpose: Opens a file for writing, appending content at the end of the file.
# Behavior:
# If the file exists, the file pointer is positioned at the end of the file, and new data will be added at the end.
# If the file does not exist, it creates a new file.
# You can only write to the file, reading is not allowed.
# The file pointer: Positioned at the end of the file.
# Example:
# python
# Copy code
# file = open("example.txt", "a")
# file.write("Appending data")
# file.close()
#
# 6. a+ (Append and Read Mode)
# Purpose: Opens a file for both appending and reading.
# Behavior:
# If the file exists, the file pointer is positioned at the end of the file.
# If the file does not exist, it creates a new file.
# Allows both reading and writing (writing always appends to the end).
# The file pointer: Positioned at the end of the file for writing, but you can move it for reading.
# Example:
# python
# Copy code
# file = open("example.txt", "a+")
# file.write("Appending new data")
# file.seek(0)  # Move pointer to the beginning for reading
# content = file.read()
# file.close()
#
# 7. x (Exclusive Creation Mode)
# Purpose: Creates a new file for writing.
# Behavior:
# If the file already exists, it raises a FileExistsError.
# If the file does not exist, it creates the file.
# You can only write to the file, reading is not allowed.
# The file pointer: Positioned at the beginning of the file.
# Example:
# python
# Copy code
# file = open("newfile.txt", "x")
# file.write("Writing to a new file")
# file.close()
# Summary Table:
# Mode	Description
# r	Read-only mode. Raises an error if the file does not exist.
# r+	Read and write mode. Raises an error if the file does not exist.
# w	Write-only mode. Creates a file if it doesn't exist, or truncates it if it does.
# w+	Read and write mode. Creates a file if it doesn't exist, or truncates it if it does.
# a	Write-only mode. Creates a file if it doesn't exist. Appends to the end of the file.
# a+	Read and write mode. Creates a file if it doesn't exist. Appends to the end of the file.
# x	Write-only mode. Creates a new file. Raises an error if the file already exists.
# These modes are useful for different scenarios depending on whether you need to read, write,
# or append data to a file, and whether you want to create or overwrite the file.

# num1 = '10'
# num2 = '5'
# p = int(num1)*int(num2)
# pr = str(p)
# print(pr)
# print(type(pr))

# print("good morning", end=" ")
# print("it is a rainy day")

# ls = [58, 555, 879, 666, 475, 58, 555, 666, 369]

# ls2 = list(filter(lambda x: (x % 2!= 0),ls))
# print(ls2)

# ls3 = list(map((lambda x: x**3),ls))
# print(ls3)

# from functools import reduce
#
# cumulative_sum = reduce((lambda x,y : x+y),ls)
# print(cumulative_sum)

# lcm of two numbers
# x = int(input("enter a value of x:"))
# y = int(input("enter a value of y:"))
#
# if x > y:
#     greater = x
# else:
#     greater = y
#
# while True:
#     if greater % x == 0 and greater % y == 0:
#         print("LCM is:", greater)
#         break
#     greater += 1

# implement a decorator @even_numbers:

# def even_num(func):
#     def wrapper(*args, **kwargs):
#         even_arg = [arg for arg in args if isinstance(arg, int) and arg % 2 == 0]
#         return func(*even_arg, **kwargs)
#
#     return wrapper
#
#
# @even_num
# def main(*numbers):
#     return f"even numbers are: {numbers}"
#
#
# print(main(58, 555, 879, 666, 475, 58, 555, 666, 369))

# find the count of upper and lower in a string

# def upper_lower(s):
#     upper_cnt = 0
#     lower_cnt = 0
#
#     for each in s:
#         if 'A' <= each <= 'Z':  #ascii value of A is 65 and 65+25=90 Z
#             upper_cnt += 1
#         elif 'a' <= each <= 'z':  #assci value of a is 67 and 67+25 = 122 z
#             lower_cnt += 1
#     return upper_cnt, lower_cnt
#
#
# print(upper_lower("pYthoN iS PYThon"))


# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         if age >= 0:
#             self._age = age
#         else:
#             raise ValueError("Age cannot be negative!")
#
# p = Person("John", 25)
# print(p.age)  # Access the age using getter
# p.age = 30  # Set the age using setter
# # p.age = -5  # This will raise a ValueError



pushing to github