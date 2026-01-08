# Sample:
# nums = [1,3,-1,-3,5,3,6,7], k = 3
# output = [1, -1, -1, 3, 5, 6]

from collections import defaultdict
import heapq
from statistics import median

class SlidingWindowMedian:
    def __init__(self):
        self.small = []   # max heap
        self.large = []   # min heap
        self.delayed = defaultdict(int)
        self.small_size = 0
        self.large_size = 0

    def prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if self.delayed[num] > 0:
                heapq.heappop(heap)
                self.delayed[num] -= 1
            else:
                break
    
    def rebalance(self):
        if self.small_size > self.large_size + 1:
            num = -heapq.heappop(self.small)
            self.small_size -= 1
            heapq.heappush(self.large,num)
            self.large_size += 1
            self.prune(self.small)
        elif self.large_size > self.small_size:
            num = heapq.heappop(self.large)
            self.large_size -= 1
            heapq.heappush(self.small, -num)
            self.small_size += 1
            self.prune(self.large)

    def remove(self, num: int):
        # since the number is going to be removed
        self.delayed[num] += 1
        
        # check which heap the num is in
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1 
            # in case the large heap is empty (cases where k = 1)
            if self.large and num == self.large[0]:
                self.prune(self.large)  
        self.rebalance()

    def add(self, num: int):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1

        self.rebalance()
    
    def median(self, k):
        if k % 2 == 0:
            return (-self.small[0] + self.large[0])/2
        else:
            return (-self.small[0])
        
def medianSlidingWindow(nums, k):
        swm = SlidingWindowMedian()
        res = []

        for i in range(len(nums)):
        
            swm.add(nums[i])

            if i >= k:
                swm.remove(nums[i - k])

            if i >= k - 1:
                res.append(swm.median(k))

        return res
    
if __name__ == '__main__':
    print(medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))