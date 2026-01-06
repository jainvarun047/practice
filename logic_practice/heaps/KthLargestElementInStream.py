# Sample:
# k = 3
# nums = [4, 5, 8, 2]

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list):
        self.k = k
        self.h = []

        for num in nums:
            heapq.heappush(self.h, num)
            if len(self.h) > k:
                heapq.heappop(self.h)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif val > self.h[0]:
            heapq.heappushpop(self.h, val)

        return self.h[0]

if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    kthLargest.add(3)   # → 4
    kthLargest.add(5)   # → 5
    kthLargest.add(10)  # → 5
    kthLargest.add(9)   # → 8
    kthLargest.add(4)   # → 8
    print(kthLargest.h)