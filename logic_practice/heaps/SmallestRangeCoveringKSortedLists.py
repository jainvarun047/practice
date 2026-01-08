import heapq

def smallestRange(nums: list[list[int]]) -> list[int]:
    heap = []
    current_max = nums[0][0]
    window = float('inf')
    
    for i,lst in enumerate(nums):
        # enter all 1st element into the heap
        heapq.heappush(heap, (lst[0], i, 0))
        if current_max < nums[i][0]:
            current_max = nums[i][0]

    res_left, res_right = 0, float('inf')
    # use the heap to avoid running infinitely
    while heap:
        val, list_num, idx = heapq.heappop(heap)
        
        # intitialize a window for compare
        current_window = current_max - val
        if current_window < window:
            window =  current_window
            res_left = val
            res_right = current_max
        
        # push the next element from the 
        # same list to further minimize window
        idx += 1
        if idx < len(nums[list_num]):
            current_max = max(current_max, nums[list_num][idx])
            heapq.heappush(heap, (nums[list_num][idx], list_num, idx))
        else:
            break
    
    return [res_left,res_right]

if __name__ == '__main__':
    print(smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
    print(smallestRange([[4,10,15,24,26],[0,9,12,20,21],[5,18,22,30]]))
    

