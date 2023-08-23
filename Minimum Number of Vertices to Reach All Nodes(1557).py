class Solution:
    def findSmallestSetOfVertices(n, edges):
        e = []
        v = []
        res = []
        for i in range(len(edges)):
            e.append(edges[i][0])
            v.append(edges[i][1])
        for i in e:
            if i not in v and i not in res:
                res.append(i)
        return res