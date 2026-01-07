
# Reference : https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem

import heapq

#
# Complete the 'runningMedian' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningMedian(arr):
    # Print your answer within the function
    small = []
    large = []
    
    for i in arr:
        heapq.heappush(small, -i)
        heapq.heappush(large, -heapq.heappop(small))
        
        if len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))
        
        res = float()
        
        if len(small) == len(large):
            res = (-small[0] + large[0])/2
        else:
            res = float(-small[0])
        print(res)

if __name__ == '__main__':
    n = int(input().strip())

    a = []

    for _ in range(n):
        a_item = int(input().strip())
        a.append(a_item)

    runningMedian(a)
