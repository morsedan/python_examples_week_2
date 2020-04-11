"""
Problem 1: Primes (15 minutes)
Break
Problem 2: Count Sort (34 minutes [first time])
Start time: 2:00pm
End time: 2:54pm (took a short break)
"""

def primes(n):
    if n <= 1:
        return None
    if n == 2:
        return [2]

    prime_list = [2]
    for number in range(3, n + 1):
        is_prime = True
        for prime in prime_list:
            if is_prime:
                if number % prime == 0:
                    is_prime = False
        if is_prime:
            prime_list.append(number)
    print(len(prime_list))
    return prime_list

print("hi")
primes(10)

def count_sort(array):
    amounts = [0 for _ in range(max(array)+1)]
    sorted_numbers = [0 for _ in range(len(array))]
    for number in array:
        amounts[number] += 1
    print("Amounts: ", amounts)
    for i in range(1,len(amounts)):
        amounts[i] = amounts[i] + amounts[i-1]
    for number in array:
        sorted_numbers[amounts[number]-1] = number
        amounts[number] = amounts[number] - 1
    print(amounts)
    return sorted_numbers

array = [4,2,2,8,3,3,1]
print(count_sort(array))

