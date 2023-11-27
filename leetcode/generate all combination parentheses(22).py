class Solution:
    def generateParenthesis(n):
        to, tc = 0, 0
        res = []
        def gp(n,tc,to):
            if (n == 0):
                return ''
            if(tc<n or to<n):
                s1 = '(' + gp(n - 1,tc,to+1)
                if (to > tc):
                    s2 = ')' + gp(n - 1,tc+1,to)
                if (len(s1) == 2 * n):
                    res.append(s1)
                if (len(s2) == 2 * n):
                    res.append(s2)
        gp(n,tc,to)
        return res
    #print(generateParenthesis(1))
    print(generateParenthesis(2))
    #print(generateParenthesis(3))


    def generateParenthesis(n):
        to, tc = 0, 0
        res = []
        if(n==1):
            return ['()']
        def gp(n,tc,to):
            if (n == 1):
                return '()'
            s1 = '(' + gp(n - 1,tc,to+1)+')'
            s2 = '('+')' + gp(n - 1,tc+1,to)
            if (len(s1) == n + n):
                res.append(s1)
            if (len(s2) == n + n):
                res.append(s2)
        gp(n,tc,to)
        return res
    #print(generateParenthesis(1))
    #print(generateParenthesis(2))
    print(generateParenthesis(3))