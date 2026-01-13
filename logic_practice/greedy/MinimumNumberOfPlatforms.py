import heapq
def stationsRequired(arr: int, dep: int) -> int:
    stations = 0

    trains = sorted(zip(arr,dep))

    if len(trains) == 0:
        return stations

    train_heap = []
    heapq.heappush(train_heap, trains[0][1])
    stations += 1

    for t in trains[1:]:
        if t[0] >= train_heap[0]:
            heapq.heappop(train_heap)
            heapq.heappush(train_heap,t[1])
        else:
            heapq.heappush(train_heap,t[1])
            stations += 1

    return stations

if __name__ == '__main__':
    print(stationsRequired([900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000]))