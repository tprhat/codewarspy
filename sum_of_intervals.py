def sum_of_intervals(intervals):  # put all of the numbers in an interval into a set, len of that is total time
    inters = []
    for s, e in intervals:
        inters += range(s, e)
    return len(set(inters))
