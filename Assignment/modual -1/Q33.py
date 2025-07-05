# Q - 33  Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4]
result = reduce(add, numbers)

print(result)
