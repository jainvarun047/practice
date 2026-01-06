# Sample:
# nums = [7, 10, 4, 3, 20, 15], k = 3
# Output: [3, 4, 7]

import heapq


def findKSmallest(arr: list, k: int) -> list:
    heap = []

    for i in arr:

        if len(heap) < k :
            heapq.heappush(heap, (-1 * i))
        elif len(heap) >= k and (-1 * heap[0]) > i:
            heapq.heappop(heap)
            heapq.heappush(heap, (-1 * i))

    return sorted(-x for x in heap)

if __name__ == '__main__':
    print(findKSmallest([7, 10, 4, 3, 20, 15],3))
        
