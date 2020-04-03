import math
from math import sqrt

"""
Rules:
1. analyze each line
2. if for-loop:
    - analyze lines inside
    - take total big(O)
    - multiply by complexity of loop
"""

# one operation O(1)
def mult_2(n):
    return n * 2

# n operations O(n)
def foo(n):
    for i in range(0, n):
        print(i)

# O(n^2)
def bar(n):
    s = 0                   # 4. O(n) * O(n) = O(n^2)
    for i in range(n):      # 3. O(n)
        for j in range(n):  # 2. O(n)
            s += i * j      # 1. O(1) (drop)
    return  s

#
def baz(n):
    s = 0                               # O(1) O(n ^ 1.5)
    for i in range(n):                  # O(n)
        for j in range(int(sqrt(n))):   # O(n^0.5)
            s += i * j                  # O(1)
    return s

def frotz(n):
    s = 0                       # O(n^2)
    for i in range(n):          # O(n)
        for j in range(2 * n):  # O(2n)
            s += i * j
    return s

def divider(n):     # O(log n) When you divide, think "log"
    while n >= 0:   # log
        n = n / 2   # O(1)

def baz(array):
    print(array[1])

    for item in array:
        item = item + 1

    for item in array:
        print(item)

def binary_search(array, value):
    start = 0
    end = len(array) - 1

    found = False

    while not found and start <= end:
        middle = (start + end) // 2

        if array[middle] == value:
            found = true
        else:
            if value < array[middle]:
                # search lower half
                end = middle -1
            else:
                # search upper half
                start = middle + 1

    return found

# SORTING
from book import Book
from copy import  deepcopy
import time
import  csv

def insertion_sort(books):
    pass