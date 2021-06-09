# Write a program that will calculate the number of trailing zeros in a factorial of a given number.
# N! = 1 * 2 * 3 * ... * N
# Be careful 1000! has 2568 digits...
# For more info, see: http://mathworld.wolfram.com/Factorial.html
# Examples
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros
import math


def zeros(n):
    trailing_zeros = 0
    if n == 0:
        return 0
    for k in range(1, math.floor(math.log(n, 5)) + 1):
        trailing_zeros += math.floor(n / pow(5, k))

    return trailing_zeros


def zeros_best_solution(n):
    x = n / 5
    return x + zeros(x) if x else 0

