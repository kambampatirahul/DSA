class Solution:
    def printFirstNegativeInteger (K,A,N):
        # code here
        neg = []
        res = []
        i = 0
        for j in range(K):
            if(A[j]<0):
                neg.append(A[j])
        while(j<N):
            if(any(neg)):
                res.append(neg[0])
                if(A[i]==neg[0]):
                    neg.pop(0)
            i+=1
            j+=1
            if(j<N and A[j]<0):neg.append(A[j])
        return res
    print(printFirstNegativeInteger(2,[-8, 2, 3, -6, 10],5))