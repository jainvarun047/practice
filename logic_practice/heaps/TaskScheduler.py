from collections import defaultdict
import heapq

def leastInterval(tasks: list[str], n: int) -> int:
    if n == 0:
        return len(tasks)
    
    d = defaultdict(int)
    for t in tasks:
        d[t] += 1
    
    heap = []
    for t in d.keys():
        heapq.heappush(heap, (-d[t], t))
    
    res = 0

    while heap:
        cycle = n+1
        used = []

        while heap and cycle > 0:
            count, task = heapq.heappop(heap)

            res += 1 # add the time to the result
            cycle -= 1 # reduce the cycle for the next element
            count += 1 # reduce the freq
            
            if -count > 0:
                # prepare for pushback onto the heap
                used.append((count, task))
        
        # push back
        for item in used:
            heapq.heappush(heap, item)
        
        # if cycle still has non-zero value
        # means there needs to be idle time added
        # but only if the heap needs to be processed again
        if heap:
            res += cycle
    return res

# Samples:
# tasks = ["A","A","A","B","B","B"]
# n = 2
# Output = 8

# tasks = ["A","A","A","B","B","B"]
# n = 0
# Output = 6

# tasks = ["A","A","A","A","B","C","D"]
# n = 2
# Output = 10


if __name__ == '__main__':
    print(leastInterval(["A","A","A","B","B","C"],2))
    print(leastInterval(["A","A","A","B","B","B"],0))
    print(leastInterval(["A","A","A","A","B","C","D"],2))