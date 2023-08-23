# class Solution:
#
#     def longestSubstring(s, k):
        # def help(ls,ma,i,j,k):
        #     di,di2,ck = {},{},0
        #     for l in range(i,ls):
        #         di2[s[l]] = di2.setdefault(s[l],0)+1
        #     # ls1=ls
        #     while(j<ls):
        #         if di2[s[j]]>=k:
        #             if(s[j] in di):
        #                 di[s[j]]+=1
        #             else:di[s[j]] = 1
        #             if(di[s[j]]==k):
        #                 ck+=1
        #             if(ck == len(di)):
        #                 ma = max(j-i+1,help(ls-j,ma,j+1,j+1,k))
        #             j+=1
        #         else:
        #             ma = max(ma,help(j-i,ma,i,i,k))
        #             j += 1
        #             i = j
        #             # ls1-=1
        #             di = {}
        #             ck = 0
        #     return ma
        # return help(len(s),0,0,0,k)
from collections import Counter
class Solution:
    def longestSubstring(s, k):
        result = 0
        for T in range(1, len(Counter(s)) + 1):
            beg, end, Found, freq, MoreEqK = 0, 0, 0, [0] * 26, 0
            while end < len(s):
                if MoreEqK <= T:
                    s_new = ord(s[end]) - 97
                    freq[s_new] += 1
                    if freq[s_new] == 1:
                        MoreEqK += 1
                    if freq[s_new] == k:
                        Found += 1
                    end += 1
                else:
                    symb = ord(s[beg]) - 97
                    beg += 1
                    if freq[symb] == k:
                        Found -= 1
                    freq[symb] -= 1
                    if freq[symb] == 0:
                        MoreEqK -= 1

                if MoreEqK == T and Found == T:
                    result = max(result, end - beg)

        return result
    print(longestSubstring('aaabb',3))
    print(longestSubstring('ababbc',2))
    print(longestSubstring('ababacb', 3))
    print(longestSubstring("bbaaacbd", 3))
    print(longestSubstring('baaabcb',3))