# Sample:
# nums = [7, 10, 4, 3, 20, 15], k = 3
# Output: [3, 4, 7]

import heapq

def findKthSmallest(arr: list, k: int) -> int:
    heap = []

    for i in arr:

        if len(heap) < k :
            heapq.heappush(heap, (-1 * i))
        elif (-1 * heap[0]) > i:
            heapq.heappop(heap)
            heapq.heappush(heap, (-1 * i))

    return -heap[0]

if __name__ == '__main__':
    print(findKthSmallest([7, 10, 4, 3, 20, 15],3))
        
