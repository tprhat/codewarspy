# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other
# elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(array):
    out = []
    zeros = 0
    for x in array:
        if x == 0:
            zeros += 1
        else:
            out.append(x)
    for i in range(zeros):
        out.append(0)
    return out
