# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers or a range of integers denoted by the starting integer separated from the end integer in the
# range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not
# considered a range unless it spans at least 3 numbers. For example "12,13,15-17" Complete the solution so that it
# takes a list of integers in increasing order and returns a correctly formatted string in the range format.
#
# Example:
#
# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-6,-3-1,3-5,7-11,14,15,17-20"

def solution(args):
    ranges = []
    i = 0
    while i < len(args):
        last_elem = args[i]
        j = 1
        for k in range(i + 1, len(args)):
            if args[k] != args[k - 1] + 1:
                break
            last_elem = args[k]
            j += 1
        if j == 1:
            ranges.append(str(args[i]))
        elif j == 2:
            ranges.extend([str(args[i]), str(last_elem)])
        else:
            ranges.append(str(args[i]) + '-' + str(last_elem))
        i += j
    return ','.join(ranges)


print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
