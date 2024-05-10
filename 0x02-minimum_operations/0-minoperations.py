#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: `Copy All` and `Paste`.

@TODO:
    Deines a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
"""


def is_prime(n, primes):
    """Function to calculate if a number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True


def prime_fact(n):
    """Function to calculate the prime factors of a number"""
    prime_factor = []
    primes = [2]
    for i in range(3, int(n**0.5) + 1, 2):
        if is_prime(i, primes):
            primes.append(i)
    for p in primes:
        while n % p == 0:
            prime_factor.append(p)
            n //= p
    if n > 1:
        prime_factor.append(n)
    return prime_factor


def minOperations(n):
    """Function to calculate the minimum operations to reach n characters"""
    if n <= 1:
        return 0
    number_operations = prime_fact(n)
    return sum(number_operations)
