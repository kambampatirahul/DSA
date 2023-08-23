class Solution:
    def climbStairs(n):
        c = 0
        mat = [-1]*n
        def cs(cu,c,mat):
            if (cu > n):
                return c
            if(mat[cu-1]!=-1):
                return mat[cu-1]
            if(cu==n):
                c+=1
                mat[cu-1] = c
                return c
            mat[cu-1] = cs(cu+1,c,mat)+cs(cu+2,c,mat)
            return mat[cu-1]
        c = cs(0,c,mat)
        return c

    print(climbStairs(2))