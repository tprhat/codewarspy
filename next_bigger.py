# Create a function that takes a positive integer and returns the next bigger number that can be formed by
# rearranging its digits. For example:
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1

def next_bigger(n):
    nums = str(n)

    swap_i = -1  # position where we have to swap
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i-1]:
            swap_i = i - 1
            break
    if swap_i == -1:
        return swap_i

    swap_j = -1  # value of next biggest number in n
    for i, d in enumerate(sorted(nums[swap_i+1:])):
        if d > nums[swap_i]:
            swap_j = d
            break
    to_swap = -1  # position of num to swap based on swap_j
    for i in range(len(nums)):
        if nums[i] == swap_j:
            to_swap = i

    swapped = ''
    for i in range(len(nums)):
        if i == swap_i:
            swapped += nums[to_swap]
        elif i == to_swap:
            swapped += nums[swap_i]
        else:
            swapped += nums[i]

    return int(swapped[:swap_i + 1] + ''.join(sorted(swapped[swap_i+1:])))


