"""
Problem 1: Bubble Sort (8 minutes)
Break
Problem 2: Merge Sort (In place)
Review:
Start time: 7:40am
End time: 8:20am
"""

def bubble_sort(arr):
    didSwap = False
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            didSwap = True
    if didSwap:
        bubble_sort(arr)

def bubble_sort(arr):
    # set up a variable to check if the swap occurred
    swap_occurred = True
    # loops through over again as long as a swap occurred
    while swap_occurred:
        # sets false as a default so the while loop breaks if the condition below doesn't pass
        swap_occurred = False
        # Loop through the array
        for i in range(0, len(arr) - 1):
            # compare each element to its neighbor
            if arr[i] > arr[i + 1]:
                # if element is in wrong position(relative to neighbor), swap them
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap_occurred = True
​
    return arr

array = [1,5,3,3,7,7,4,2,6,4]
bubble_sort(array)
print(array)

def merge_sort(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
    arr[0] = merge_sort(arr[:len(arr) // 2])
    arr[1] = merge_sort(arr[len(arr) // 2:])
    temp_arr = []
    while len(arr[0]) > 0 and len(arr[1]) > 0:# for i in range(arr[0]):
        if len(arr[0]) == 0:
            temp_arr += arr[1]
        if len(arr[1]) == 0:
            temp_arr += arr[0]
        if arr[0][0] < arr[1][0]:
            temp_arr.append(arr[0][0])
        else:
            temp_arr.append(arr[1][0])

    return temp_arr

my_array = [3, 2, 1]
print(my_array)
merge_sort(my_array)
print(my_array)
