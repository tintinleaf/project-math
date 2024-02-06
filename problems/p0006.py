#!/usr/bin/env python3
# coding: utf-8

"""

Sum Square Difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + … + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + … + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

PID = 6
ANSWER = 25164150
number = 100


def solve_1():
    n = number
    sum_of_squares = sum(i**2 for i in range(1, n+1))
    square_of_sum = sum(range(1, n+1))**2

    return square_of_sum - sum_of_squares

def solve_2():
    n = number
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    square_of_sum = (n * (n + 1) // 2) ** 2

    return square_of_sum - sum_of_squares

def solve_3():
    n = number
    return (n * (n + 1) * (3 * n**2 - n - 2)) // 12



