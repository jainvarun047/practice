from collections import defaultdict


def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        # If we see a duplicate, shrink the window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add the current character and update max
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
        
    return max_len

if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))
    print(lengthOfLongestSubstring('pwwkew'))
    print(lengthOfLongestSubstring('dvdf'))
            
