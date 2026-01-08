import heapq
def minCostToConnectRopes(ropes: list[int]) -> int:
    if not ropes:
        return 0
    
    if len(ropes) < 3:
        return ropes[0] if (len(ropes) ==1 ) else ropes[0] + ropes[1]

    res = 0
    heap = []
    for i in ropes:
        heapq.heappush(heap, i)
    
    while len(heap) > 1:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        res += num1 + num2
        heapq.heappush(heap, num1 + num2)

    return res

# Sample:
# ropes = [4, 3, 2, 6]
# 29

if __name__ == '__main__':
    print(minCostToConnectRopes([4, 3, 2, 6]))