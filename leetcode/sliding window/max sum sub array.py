class Solution:
    def maximumSumSubarray (K,Arr,N):
        # code here
        sum = 0
        i = 0
        for j in range(K):
            sum+=Arr[j]
        ma = sum
        while(j<N-1):
            sum-=Arr[i]
            i+=1
            j+=1
            sum+=Arr[j]
            ma = max(sum,ma)
        return ma
    print(maximumSumSubarray(2,[100,200,300,400],4))