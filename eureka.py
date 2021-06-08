# The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the
# title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number.
#
# In effect: 89 = 8^1 + 9^2
#
# The next number in having this property is 135.
#
# See this property again: 135 = 1^1 + 3^2 + 5^3
#
# We need a function to collect these numbers, that may receive two integers a, b that defines the range [a,
# b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    output = []
    for x in range(a, b + 1):
        i = 1
        s = 0
        for y in str(x):
            s += int(y) ** i
            i += 1
        if x == s:
            output.append(x)
    return output


print(sum_dig_pow(1, 10))


# best solution

def filter_func(a):
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow_best(a, b):
    return filter(filter_func, range(a, b+1))
