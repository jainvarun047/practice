

import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (store negatives)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # Step 1: push to max heap
        heapq.heappush(self.small, -num)

        # Step 2: ensure ordering invariant
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: rebalance sizes
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

        
if __name__ == '__main__':
    mf = MedianFinder()

    mf.addNum(1)
    print(mf.findMedian())    # expected → 1

    mf.addNum(2)
    print(mf.findMedian())    # expected → 1.5

    mf.addNum(3)
    print(mf.findMedian())    # expected → 2

    mf.addNum(4)
    print(mf.findMedian())   # expected → 2.5

    mf.addNum(0)
    print(mf.findMedian())    # expected → 2