"""
Problem 1:
Break
Problem 2:
Review: Primes (),
Start time: 7:55am
End time:
"""
def sieve(number, factor=2):
    if number <= 1:
        return []
    primes = [num for num in range(2,number+1)]
    return eliminate_factors(primes, factor)

def eliminate_factors(numbers, factor):
    if factor >= max(numbers) // 2:
        return numbers
    primes = [num for num in numbers if num == factor or num % factor != 0]
    while True:
        factor += 1
        if factor in primes and factor <= max(numbers):
            break
    eliminate_factors(primes, factor)


print("sieve", sieve(100))
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

print(primes(100))