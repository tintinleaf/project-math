#!/usr/bin/env python3
# coding: utf-8

"""
Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(1, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1
    while d == 1:
        x = (x**2 + c) % n
        y = (y**2 + c) % n
        y = (y**2 + c) % n
        d = gcd(abs(x - y), n)
    return d

def largest_prime_factor(n):
    if n == 1:
        return None
    if n == 2:
        return 2
    factor = pollards_rho(n)
    while factor < n:
        n //= factor
        factor = pollards_rho(n)
    return n

number = 600851475143
result = largest_prime_factor(number)
print(f"The largest prime factor of {number} is: {result}")


"""

ANSWER = 6857
number = 600851475143

def solve():
    n = number
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n




