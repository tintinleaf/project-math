#!/usr/bin/env python3
# coding: utf-8

"""

Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers 1 from 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

import math

PID = 5
ANSWER = 232792560
number = 20

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def solve_1():
    n = number
    result = 1

    for i in range(2, n + 1):
        result = lcm(result, i)
    return result

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def solve_2():
    result = 1
    n = number
    primes = [i for i in range(2, n+1) if is_prime(i)]

    for p in primes:
        x = math.floor(math.log(n, p))
        result *= p ** x

    return result







