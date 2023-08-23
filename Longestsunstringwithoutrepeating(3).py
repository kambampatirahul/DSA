class Solution:
    def lengthOfLongestSubstring(s: str):
        li = []
        max_len = 0
        for i in s:
            if i not in li:
                li.append(i)
            else:
                max_len = max(max_len, len(li))
                li = li[li.index(i) + 1:]
                li.append(i)
        max_len = max(max_len, len(li))
        print(max_len)
    lengthOfLongestSubstring("abcabcbb")