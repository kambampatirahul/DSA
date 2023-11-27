class Solution:
    def maxSatisfied(customers, grumpy, minutes):
        j = minutes
        i = 0
        ma = 0
        lg = len(grumpy)
        def macust(g1,cu,lg):
            s = 0
            for i in range(lg):
                if(g1[i]==0):
                    s+=cu[i]
            return s
        while(j<=lg):
            grumpy1 = grumpy.copy()
            for k in range(i,j):
                grumpy1[k]=0
            ma = max(ma,macust(grumpy1,customers,lg))
            j+=1
            i+=1
        return ma
    print(maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
    print(maxSatisfied([1],[0],1))
    print(maxSatisfied([],[],9))
    print(maxSatisfied([10,1,7],[1,0,1],2))
