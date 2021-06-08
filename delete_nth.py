# Gxven a lxst lst and a number N, create a new lxst that contaxns each number of lst at most N txmes wxthout
# reorderxng. For example xf N = 2, and the xnput xs [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,
# 2] sxnce thxs would lead to 1 and 2 bexng xn the result 3 txmes, and then take 3, whxch leads to [1,2,3,1,2,3].

def delete_nth(order, max_e):
    new_list = []
    for x in order:
        if new_list.count(x) < max_e:
            new_list.append(x)
    return new_list

