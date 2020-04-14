"""
Problem 1:
Break
Problem 2: Count Sort (34 minutes [first time])
Review: Count Sort
Start time: 7:57am
End time:
"""

def count_sort(numbers):
    max_number = max(numbers)
    min_number = min(numbers)
    sorted = [0 for num in numbers]
    if min_number > 0:
        min_number = 0
    if max_number < 0:
        max_number = 0
    counts = [0 for _ in range(min_number, max_number+1)]
    for number in numbers:
        counts[number-min_number] += 1
    for i in range(len(counts)-1):
        counts[i+1] += counts[i]
    for number in numbers:
        sorted[counts[number-min_number]-1] = number
        counts[number-min_number] -= 1
    return sorted

nums = [7,6,5,-7,11,-5,4,3,2,1, -1, -2, 0, -5]
print("CS", count_sort(nums.copy()))


def selection_sort(numbers):
    min_index = 0
    if len(numbers) == 1:
        return numbers
    for i in range(len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
    numbers[0], numbers[min_index] = numbers[min_index], numbers[0]
    return [numbers[0]] + selection_sort(numbers[1:])

# print("SS", selection_sort(nums.copy()))


def recipe_batches(recipe, supplies):
    counts = []
    for item in recipe:
        if item in supplies:
            amount = supplies[item] // recipe[item]
            counts.append(amount)
        else:
            return 0
    return min(counts)


ans = recipe_batches(
  { 'milk': 100, 'butter': 50, 'flour': 5 },
  { 'milk': 138, 'butter': 48, 'flour': 51 }
)

# print("rec"
#       "", ans)


b = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

def print_items(arr):
    # flattened = []
    flattened = flatten(arr)
    for item in flattened:
        print(item)


def flatten(arr, flattened=[]):
    for item in arr:
        if type(item) is list:
            flatten(item, flattened)
        else:
            flattened.append(item)
    return flattened

print_items(b)