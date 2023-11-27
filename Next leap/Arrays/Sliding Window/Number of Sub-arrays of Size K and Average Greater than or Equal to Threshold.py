'''
Problem Description
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

Example 2:
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
'''

def greaterthenthreshold(nums,k,t):
    s=c=j=i=0
    while(j<k):
        s+=nums[j]
        j+=1
    if s/k >= t :c+=1
    while(j<len(nums)):
        s+=nums[j]
        s-=nums[i]
        if s / k >= t: c += 1
        i+=1
        j+=1
    return c

print(greaterthenthreshold([2,2,2,2,5,5,5,8],3,4))
print(greaterthenthreshold([11,13,17,23,29,31,7,5,2,3],3,5))