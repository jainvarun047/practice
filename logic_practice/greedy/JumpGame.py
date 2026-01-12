def canJump(nums: list[int]) -> bool:
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + nums[i])

        if (max_reach >= len(nums)-1):
            return True
    
    return False


# Example
# nums = [2,3,1,1,4]
# Output: True
# nums = [3,2,1,0,4]
# Output: False

if __name__ == '__main__':
    print(canJump([2,3,1,1,4]))
    print(canJump([3,2,1,0,4]))