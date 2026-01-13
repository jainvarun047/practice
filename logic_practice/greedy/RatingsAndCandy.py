def candyCounts(ratings: list) -> int:

    n = len(ratings)
    candy = [1] * n
    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            candy[i] = max(candy[i], candy[i-1]+1)

    for i in range(n-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            candy[i] = max(candy[i], candy[i+1]+1)

    total = sum(candy)
    return total

if __name__ == '__main__':
    print(candyCounts([1, 0, 2]))
    print(candyCounts( [1, 2, 2]))
    print(candyCounts([1, 2, 3, 1]))
    print(candyCounts([5,4,3,2,1]))