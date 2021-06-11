# Write a function that counts how many different ways you can make change for an amount of money, given an array of
# coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:
# 1+1+1+1, 1+1+2, 2+2.
# The order of coins does not matter:
# 1+1+2 == 2+1+1
# Also, assume that you have an infinite amount of coins.
# Your function should take an amount to change and an array of unique denominations for the coins:
#   count_change(4, [1,2]) # => 3
#   count_change(10, [5,2,3]) # => 4
#   count_change(11, [5,7]) # => 0

# dynamic programing
def count_change(money, coins):
    m = len(coins)
    table = [[0 for _ in range(m)] for _ in range(money + 1)]

    # Fill the entries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    for i in range(1, money + 1):
        for j in range(m):
            # Count of solutions including coins[j]
            x = table[i - coins[j]][j] if i - coins[j] >= 0 else 0
            # Count of solutions excluding coins[j]
            y = table[i][j - 1] if j >= 1 else 0
            # total count
            table[i][j] = x + y
    return table[money][m - 1]

# recursion
def count_change_recursion(money, coins):
    if money < 0:
        return 0
    if money == 0:
        return 1
    if money > 0 and not coins:
        return 0
    return count_change(money - coins[-1], coins) + count_change(money, coins[:-1])
