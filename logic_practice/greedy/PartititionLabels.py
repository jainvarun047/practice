from collections import defaultdict


def partitionLabels(s: str) -> list[int]:
    if not s:
        return []
    
    chars = defaultdict(int)

    for i,c in enumerate(s):
        chars[c] = i
    
    start = 0
    end = 0
    res = []
    for i,c in enumerate(s):
        end = max(end, chars[c])
        if i == end:
            res.append((end-start) + 1)
            start = i+1
    
    return res

# Example
# s = "ababcbacadefegdehijhklij"
# Output:
# [9, 7, 8]

if __name__ == '__main__':
    print(partitionLabels("ababcbacadefegdehijhklij"))
    print(partitionLabels("eccbbbbdec"))