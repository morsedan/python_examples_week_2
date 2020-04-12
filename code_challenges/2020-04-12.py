"""
Problem 1: Rock, Paper, Scissors
Break 8:15, 8:30
Problem 2: Fibonacci
Start time: 8:10
End time:
"""

def rps_permutations(number):
    choices = ["rock", "paper", "scissors"]

    possibilities = [[] for _ in range(3 ** number)]
    first_break_index = len(possibilities) // 3
    second_break_index = first_break_index * 2

    for i in range(len(choices)):
        for j in range(0, first_break_index):
            possibilities[j].append(choices[i])
        i = increment(i)
        print(i)
        for j in range(first_break_index, second_break_index):
            possibilities[j].append(choices[i])
        i = increment(i)
        for j in range(second_break_index, len(possibilities)):
            possibilities[j].append(choices[i])

    # for j in range(0, first_break_index):
    #     possibilities[j].append(choices[0])
    # for j in range(first_break_index, second_break_index):
    #     possibilities[j].append(choices[1])
    # for j in range(second_break_index, len(possibilities)):
    #     possibilities[j].append(choices[2])
    # for i in range(len(choices)):
        # for j in range(0, first_break_index):
        #     possibilities[j].append(choices[i])
        # for j in range(first_break_index, second_break_index):
        #     possibilities[j].append(choices[i])

    return possibilities

def increment(i):
    if i == 2:
        return 0
    return i + 1

print(rps_permutations(2))

def fibonacci(n):
    if n < 2:
        return n
    first = 0
    second = 1
    for i in range(n-1):
        temp = second
        second += first
        first = temp
        print(first, second)
    return second

print(fibonacci(2))
