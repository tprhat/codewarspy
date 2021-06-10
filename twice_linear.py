# Consider a sequence u where u is defined as follows:
# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Example:
# u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]
# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
# Task: Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered sequence
# u (ordered with < so there are no duplicates) .
# Example:
# dbl_linear(10) should return 22
# Note:
# Focus attention on efficiencyx


from collections import deque


def dbl_linear(n):
    u = [1]
    u_temp = u.copy()
    while len(list(set(u))) <= 5 * n:  # 5 * n allows finding the correct order for large n, gross
        temp = []
        for i in u_temp:
            y = 2 * i + 1
            z = 3 * i + 1
            temp.extend([y, z])
        u_temp.clear()
        u.extend(temp)
        u_temp.extend(temp)
    u = list(set(u))
    u.sort()
    return u[n]


def dbl_linear_bestsolution(n):
    h = 1
    cnt = 0
    q2, q3 = deque([]), deque([])
    while True:
        if cnt >= n:
            return h
        q2.append(2 * h + 1)
        q3.append(3 * h + 1)
        h = min(q2[0], q3[0])
        if h == q2[0]:
            h = q2.popleft()
        if h == q3[0]:
            h = q3.popleft()
        cnt += 1
