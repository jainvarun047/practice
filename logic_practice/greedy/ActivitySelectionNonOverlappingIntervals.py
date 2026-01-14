def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    # return the maximum number of intervals to non-overlapping intervals

    if not intervals:
        return 0
    
    # 1. Sort by end time
    intervals.sort(key = lambda x: x[1])

    # pick the first one
    kept = 1
    prev_end = intervals[0][1]

    # Greedily select intervals
    for start,end in intervals[1:]:
        if start >= prev_end:
            kept+= 1
            prev_end = end
    
    return len(intervals)-kept # or kept in case you want the non overlapping ones.
    


