'''
Problem Description
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''

def foursome(nums,t):
    nums.sort()
    fourlet = []
    length = len(nums)
    for l in range(length-2):
        if l != 0 and nums[l] == nums[l - 1]: continue
        for i in range(l+1,length - 1):
            if i-1!=l and nums[i] == nums[i - 1]: continue
            c = nums[i]+nums[l]
            T = t - c
            k = i + 1
            j = len(nums) - 1
            while (k < j):
                temp = nums[k] + nums[j]
                if (temp > T):
                    j -= 1
                elif (temp < T):
                    k += 1
                else:
                    fourlet.append([nums[l],nums[i], nums[k], nums[j]])
                    j -= 1
                    while(nums[k]==nums[k+1] and k<j):k+=1
                    k+=1
                    while nums[j] == nums[j + 1] and i < j: j -= 1
    return fourlet

print(foursome([1,0,-1,0,-2,2],0))
print(foursome([2,2,2,2,2],8))