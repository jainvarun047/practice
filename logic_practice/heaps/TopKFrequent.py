# Sample:
# nums = [1,1,1,2,2,3]
# k = 2
# Output: [1, 2]

import heapq

def topKFrequent(nums: list, k: int) -> list:
    h = []
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    for i in d.keys():
        heapq.heappush(h, (d[i],i))
        if len(h) > k:
            heapq.heappop(h)
    
    return [j for i,j in h]
    
if __name__ == '__main__':
    print(topKFrequent([1,1,1,2,2,3],2))