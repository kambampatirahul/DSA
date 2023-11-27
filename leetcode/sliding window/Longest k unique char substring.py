class Solution:

    def longestKSubstr(s, k):
        # code here
        ma,c,d,j=-1,0,{},0
        for i in range(len(s)):
            if s[i] in d.keys():
                d[s[i]]+=1
            else:
                c+=1
                d[s[i]]=1
            if c==k:ma = max(ma,i-j+1)
            while(c>k):
                if s[j] in d.keys():
                    if(d[s[j]]==1):
                        d.pop(s[j])
                        c-=1
                    else:d[s[j]] -= 1
                j+=1
        return ma
    print(longestKSubstr('aabacbebebe',3))
    print(longestKSubstr('ji',2))