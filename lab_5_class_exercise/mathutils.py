def is_even(n):
    return n % 2 == 0  # True if n is divisible by 2


def factorial(n):
    if n < 0:
        raise ValueError("Negative not allowed")
    result = 1
    for i in range(2, n + 1):  # multiply 1 * 2 * 3 * ... * n
        result *= i
    return result
