class Solution:
    def mostPoints(questions):
        l = len(questions)
        # matrix = [-1 for i in range(l)]
        # def mp(j):
        #     if(j<0 or j>=l):
        #         return 0
        #     if(matrix[j]!=-1):
        #         return matrix[j]
        #     matrix[j] = max(questions[j][0]+mp(1+j+questions[j][1]),mp(j+1))
        #     return matrix[j]
        # return mp(0)

        matrix = [l]


    print(mostPoints([[3,2],[4,3],[4,4],[2,5]]))
    print(mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))