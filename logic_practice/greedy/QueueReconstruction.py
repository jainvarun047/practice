def reconstruct(heights: list) -> list:
    heights.sort( key=lambda x: (-x[0], x[1]))

    res = []
    for i in range(len(heights)):
        res.insert(heights[i][1],heights[i])

    return res

if __name__ == '__main__':
    print(reconstruct([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))