def jump(nums: list[int]) -> int:
    current_end = 0
    farthest = 0
    jumps = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest,i + nums[i])

        if i == current_end:
            jumps += 1
            current_end = farthest
    
    return jumps
        
        


# Example
# nums = [2,3,1,1,4]
# Output: 2

if __name__ == '__main__':
    print(jump([2,3,1,1,4]))
    print(jump([1,4,1,1,1,1]))
    print(jump([1,1,1,1]))
    print(jump([5,1,1,1,1]))
    print(jump([2,1,3,1,1,1]))