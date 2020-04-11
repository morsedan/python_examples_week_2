def nth_fib(n):
    if n < 2:
        return n
    return nth_fib(n - 1) + nth_fib(n - 2)

# print(nth_fib(35))

def nth_fib_cache(n, cache):
    if n < 2:
        return n
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] = nth_fib_cache(n-1, cache) + nth_fib_cache(n-2, cache)
        return cache[n]

n = 1
cache = [0 for _ in range(n+1)]
print(nth_fib_cache(n, cache))

def iterative_fib(n):
    answer = 0
    n_1 = 1
    n_2 = 0
    for i in range(n-1):
        answer = n_1 + n_2
        n_2 = n_1
        n_1 = answer
    return answer

# print(iterative_fib(100000))


def find_subarray(arr, sum):
    for i in range(len(arr)):
        total = arr[i]
        for j in range(i+1,len(arr)):
            if total == sum:
                return (i, j)
            if total < sum:
                total += arr[j]
    return None


def fast_find_subarray(arr, sum):
    start_index = 0
    end_index = 1
    total = arr[start_index]

    if total == sum:
        return (start_index, start_index)

    total += arr[end_index]

    while start_index < len(arr) and end_index < len(arr):
        if total == sum:
            return (start_index, end_index)
        if total < sum:
            end_index += 1
            total += arr[end_index]
        if total > sum:
            total -= arr[start_index]
            start_index += 1


    return None


# print(fast_find_subarray([1, 4, 20, 3, 10, 5], 33))
# print(fast_find_subarray([1, 4, 0, 0, 3, 10, 5], 7))
# print(fast_find_subarray([1, 4], 0))
# print(fast_find_subarray([33], 33))

import unittest
import time
class Test(unittest.TestCase):
    def test_find_subarray(self):
        start_time = time.time()
        self.assertEqual(find_subarray([1, 4, 20, 3, 10, 5], 33), (2, 4))
        self.assertEqual(find_subarray([1, 4, 0, 0, 3, 10, 5], 7), (1, 4))
        self.assertEqual(find_subarray([1, 4], 0), None)
        end_time = time.time()
        print(f"runtime: {end_time - start_time} miliseconds\n")



def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

fizzBuzz(15)

# [1, 4, 20, 3, 10, 5], sum = 33 # (2, 4)
# [1, 4, 0, 0, 3, 10, 5] sum = 7 # (1, 4)