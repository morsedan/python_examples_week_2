def n_demo(n):      # O(n)
    print(n)
    if n == 0:
        return
    n_demo(n - 1)

def two_n_demo(n):
    print(n)
    if n == 0:
        return
    two_n_demo(n - 1)
    two_n_demo(n - 1)

def divide_n_demo(n):
    print(n)
    if n <= 1:
        return
    divide_n_demo(n / 2)
    divide_n_demo(n / 2)

two_n_demo(5)
divide_n_demo(16)