class Solution:
    def minWindow(s, t):
        dt,j,mis,mi = {},0,'',1000000
        for i in t:
            dt[i] = dt.setdefault(i,0)+1
        ldt = len(dt)
        i=0
        while(j<len(s)):
            if s[j] in dt:
                dt[s[j]]-=1
                if dt[s[j]]==0:
                    ldt-=1
            if ldt == 0:
                while(1):
                    if(mi>j-i+1):
                        mis = s[i:j+1]
                        mi = j-i+1
                    if s[i] in dt:
                        if dt[s[i]]<0:
                            dt[s[i]]+=1
                        else:break
                    i+=1
            j+=1
        return mis
    print(minWindow('bba','ab'))
    print(minWindow('ADOBECODEBANC','ABC'))
    print(minWindow('a','a'))
    print(minWindow('a','aa'))