'''
Problem Description
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

def repeatingchar(s,k):
    di,mf,j,l = {},0,0,0
    for i in range(len(s)):
        di[s[i]]=di.setdefault(s[i],0)+1
        mf = max(mf,di[s[i]])
        if(i-j+1-mf<=k):l = max(l,i-j+1)
        else:
            mf-=1
            if di[s[j]]==1:del di[s[j]]
            else:di[s[j]]-=1
            j+=1
        i+=1
    return l

print(repeatingchar("AABABBA",1))
print(repeatingchar("ABAB",2))