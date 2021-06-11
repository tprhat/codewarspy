# For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))). E. g.,
# last_digit([3, 4, 2]) == 1 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721. Beware: powers grow incredibly fast. For
# example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.
# Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.

# every number has cyclic last num after pow()
# 0:[0,0,0,0]
# 1:[1,1,1,1]
# 2:[2,4,8,6]
# 3:[3,9,7,1]
# 4:[4,6,4,6]
# 5:[5,5,5,5]
# 6:[6,6,6,6]
# 7:[7,9,3,1]
# 8:[8,4,2,6]
# 9:[9,1,9,1]

def last_digit(lst):
    n = 1
    for x in reversed(lst):
        print(n)
        n = x ** (n if n < 4 else n % 4 + 4)
        print(n)
        print(n % 4)
    return n % 10

