# Sample:
# lists = [
#     [1, 4, 5],
#     [1, 3, 4],
#     [2, 6]
# ]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]

import heapq

def mergeKSortedLists(lists: list[list[int]]) -> list:
    min_heap = []
    result = []

    # Step 1: push first element of each list
    for list_idx, lst in enumerate(lists):
        if lst:  # handle empty lists
            heapq.heappush(min_heap, (lst[0], list_idx, 0))

    # Step 2: extract min and push next from same list
    while min_heap:
        val, list_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            next_val = lists[list_idx][next_idx]
            heapq.heappush(min_heap, (next_val, list_idx, next_idx))

    return result

if __name__ == '__main__':
    mergeKSortedLists([[1, 4, 5],[1, 3, 4],[2, 6]])

 