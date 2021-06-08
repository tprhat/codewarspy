#  recursively sum digits in a number until the sum is less than 10

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


print(digital_root(943))
