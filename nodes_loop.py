# https://en.wikipedia.org/wiki/Cycle_detection
# You are given a node that is the beginning of a linked list. This
# list always contains a tail and a loop. Your objective is to determine the length of the loop.
#
# Use the `next' attribute to get the following node
# node.next
# Note: do NOT mutate the nodes!
# Thanks to shadchnev, I broke all of the methods from the Hash class.
# Don't miss dmitry's article in the discussion after you pass the Kata !!
def loop_size(node):
    c = 0
    visited = {[]}
    while True:
        x = node.next
        if x not in visited:
            visited.add(x)
        else:
            c = list(visited).index(x)
            c = len(visited) - len(visited[:c])
            break
    return c
