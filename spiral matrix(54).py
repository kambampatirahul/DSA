import math
class Solution:
    # def spiralOrder(matrix):
    #     rc,cc,i,j=0,1,0,0
    #     l = len(matrix)
    #     mc = len(matrix[0])-1
    #     mr = l-1
    #     res=[]
    #     a=math.ceil(l/2)
    #     while(a>=0):
    #         while(j<=mc):
    #             res.append(matrix[i][j])
    #             j+=1
    #         mc-=1
    #         j-=1
    #         i+=1
    #         while(i<mr):
    #             res.append(matrix[i][j])
    #             i+=1
    #         mr-=1
    #         while (j>=0+cc):
    #             res.append(matrix[i][j])
    #             j-=1
    #         rc+=1
    #         j+=1
    #         i-=1
    #         while (i>0+rc):
    #             res.append(matrix[i][j])
    #             i-= 1
    #         cc += 1
    #         a-=1
    #     print(res)
    # spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    # spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    # def spiralOrder(matrix):
    #     r = len(matrix)-1
    #     c = len(matrix[0])-1
    #     res = []
    #     i,j=0,0
    #     if(r==0):res=matrix[0]
    #     elif(c==0):
    #         for i in matrix:
    #             res.append(i[0])
    #     else:
    #         if(r>=c):n=math.floor((c+1) / 2) + 1
    #         else: n=math.floor(r / 2) + 1
    #         for k in range(n):
    #             z = 0
    #             x = 0
    #             while (j <= c - k):
    #                 res.append(matrix[i][j])
    #                 j += 1
    #                 x = 1
    #             j -= 1
    #             i += 1
    #             while (i <= r - k and c-k>0):
    #                 res.append(matrix[i][j])
    #                 i += 1
    #                 z = 1
    #             i -= 1
    #             j -= 1
    #             while (j >= 0 + k and z == 1):
    #                 res.append(matrix[i][j])
    #                 j -= 1
    #             j += 1
    #             i -= 1
    #             while (i > 0 + k + 1 and x == 1):
    #                 res.append(matrix[i][j])
    #                 i -= 1
    #     print(res)
    def spiralOrder(matrix):
        rt, lt, rb, lb = len(matrix[0]) - 1, 0, len(matrix) - 1, 0
        res = []
        while (lt <= rb and lb <= rt):
            t = lt
            while (t < rt + 1):
                res.append(matrix[lt][t])
                t += 1
            lt += 1
            t = lt
            while (t < rb + 1 and lt <= rb and lb <= rt):
                res.append(matrix[t][rt])
                t += 1
            rt -= 1
            t = rt
            while (t > lb - 1 and lt <= rb and lb <= rt):
                res.append(matrix[rb][t])
                t -= 1
            rb -= 1
            t = rb
            while (t > lt - 1 and lt <= rb and lb <= rt):
                res.append(matrix[t][lb])
                t -= 1
            lb += 1
        print(res)

    spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    spiralOrder([[6,9,7]])
    spiralOrder([[7],[9],[6]])
    spiralOrder([[2,5,8],[4,0,-1]])
    spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
    spiralOrder([[1,2,3,4,5,6,7,8,9,10]])
    spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])
