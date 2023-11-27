'''
Problem Description
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
'''

def subarraysum(nums,k):
    i=s=c=0
    di = {0:1}
    while(i<len(nums)):
        s+=nums[i]
        if s-k in di:c+=di[s-k]
        if s not in di:di[s]=1
        else:di[s]+=1
        i+=1
    return c

print(subarraysum([1,2,3],3))
print(subarraysum([1,1,1],2))
print(subarraysum([10, 2, -2, -20, 10],-10))