'''
Problem Description
Given a string you need to return the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.

Example 1:
Input: s = "aabacbebebe", k = 3
Output: 7
Explanation: "cbebebe" is the longest substring with K distinct characters.

Example 2:
Input: s = "aaaa", k = 2
Output: -1
Explanation: There's no substring with K distinct characters.
'''

def longestunique(s,k):
    u = {}
    i=j=uni=0
    l=-1
    n=len(s)
    while(j<n):
        if s[j] in u: u[s[j]]+=1
        else:
            u[s[j]] = 1
            uni+=1
        if(uni>=k):
            l = max(l,j+1-i)
            while(uni>k and i<j):
                if u[s[i]] == 1:
                    uni-=1
                    del u[s[i]]
                else:u[s[i]]-=1
                i+=1
        j+=1
    return l

print(longestunique("aabacbebebe",3))
print(longestunique("aaaa",2))