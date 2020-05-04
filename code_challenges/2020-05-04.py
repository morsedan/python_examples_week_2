"""
Problem 1: selectin sort
Break
Problem 2: none
Start time: ??
End time: ??
"""


def selection_sort(arr):
    if len(arr) == 1:
        return arr
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    arr[0], arr[min_index] = arr[min_index], arr[0]
    return [arr[0]] + selection_sort(arr[1:])


array = [5, 4, 3, 2, 1]
print(selection_sort(array))
