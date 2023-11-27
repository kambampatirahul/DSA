class Solution:
    def longestOnes(nums, k):
        i=c0=j=ma=0
        while(j<len(nums)):
            if(nums[j]==0):
                c0+=1
            if c0<=k:
                ma = max(ma,j-i+1)
            if c0>k:
                if nums[i]==0:
                    c0-=1
                i+=1
            j += 1
        return ma
    print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
    print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
    print(longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1], 2))
    print(longestOnes([1, 1, 1, 0, 0, 1, 1, 1, 1], 2))
    print(longestOnes([0,0,0,1,0,0,1],4))
    print(longestOnes([1, 1, 0, 1], 0))


