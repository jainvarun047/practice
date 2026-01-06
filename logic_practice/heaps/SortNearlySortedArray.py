
# Sample:
# nums = [6, 5, 3, 2, 8, 10, 9]
# k = 3

import heapq

def sortKSortedArray(arr: list, k: int) -> list:
    res = []
    h=[]

    for i in arr:
        heapq.heappush(h, i)
        if len(h) > k:
            res.append(heapq.heappop(h))
    
    while h:
        res.append(heapq.heappop(h))

    return res

if __name__ == '__main__':
    print(sortKSortedArray([6, 5, 3, 2, 8, 10, 9],3))
        