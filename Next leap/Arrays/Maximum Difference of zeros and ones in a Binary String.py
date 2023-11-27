'''
Problem Description
Given a binary string s of 0's and 1's. The task is to find the maximum difference between the number of 0s and the number of 1s (number of 0s — number of 1s) for a substring . In case of all 1s print -1.

Example 1:
Input: s = "11000010001"
Output: 6
Explanation: From index 2 to index 9, there are 7 0s and 1 1s, so number of 0s - number of 1s is 6.

Example 2:
Input: s = "11"
Output: -1
'''

def maxdiff(s):
    i = co = cz = 0
    d = -1
    while i <= len(s) - 1:
        if s[i] == '0': cz += 1
        else: co += 1
        if cz - co > 0:d = max(d, cz - co)
        else:cz = co = 0
        i += 1
    return d

print(maxdiff("1100001000100000"))
print(maxdiff("0011"))
print(maxdiff("11000000000010001"))
print(maxdiff("111"))
print(maxdiff("0000"))
print(maxdiff("10001100"))
print(maxdiff("1100"))
print(maxdiff("011111010011"))