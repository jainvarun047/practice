def findMinArrowShots(points: list[list[int]]) -> int:
    if not points:
        return 0
    
    points.sort(key=lambda x: x[1])

    arrows = 1
    prev_end = points[0][1]

    for start,end in points[1:]:
        if start > prev_end:
            arrows += 1
            prev_end = end

    return arrows

# Example
# balloons = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2

if __name__ == '__main__':
    print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
    print(findMinArrowShots([[1,2],[2,3],[3,4],[1,3]]))