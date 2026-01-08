import heapq
from collections import defaultdict

def reorganizeString(s: str) -> str:
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1

    heap = []
    for c, f in freq.items():
        heapq.heappush(heap, (-f, c))

    res = []

    while len(heap) > 1:
        f1, c1 = heapq.heappop(heap)
        f2, c2 = heapq.heappop(heap)

        res.append(c1)
        res.append(c2)

        if f1 + 1 < 0:
            heapq.heappush(heap, (f1 + 1, c1))
        if f2 + 1 < 0:
            heapq.heappush(heap, (f2 + 1, c2))

    if heap:
        f, c = heap[0]
        if -f > 1:
            return ""
        res.append(c)

    return "".join(res)


if __name__ == '__main__':
    print(reorganizeString("aab"))
    print(reorganizeString("aaabbc"))
    print(reorganizeString("vvvlo"))
    print(reorganizeString("aabbcc"))
    print(reorganizeString("aaab"))
        
