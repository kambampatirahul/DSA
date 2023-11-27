class Solution:
    def minRemoveToMakeValid(s: str):
        o,b=0,0
        cs=s
        for i in range(len(s)):
            if s[i]=='(':
                o+=1
            elif s[i]==')':
                if(o==0):
                    cs=cs[:i-b]+cs[i+1-b:]
                    b+=1
                else: o-=1
        j = len(cs)-1
        while(o!=0 and j>=0):
            if(cs[j]=='('):
                cs = cs[:j]+cs[j+1:]
                o-=1
            j-=1
        print(cs)
    minRemoveToMakeValid("lee(t(c)o)de)")
    minRemoveToMakeValid("a)b(c)d")
    minRemoveToMakeValid("))((")
    minRemoveToMakeValid("(a(b(c)d)")