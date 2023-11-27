'''
Problem Description
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

def threesum(nums,t):
    nums.sort()
    triplet = []
    for i in range(len(nums)-1):
        # if nums[i]>0:break
        if i!=0 and nums[i] == nums[i-1]:continue
        c = nums[i]
        T = t-c
        k = i+1
        j = len(nums)-1
        while (k < j):
            temp = nums[k] + nums[j]
            if (temp > T):
                j -= 1
            elif (temp < T):
                k += 1
            else:
                triplet.append([nums[i], nums[k], nums[j]])
                j -= 1
                while nums[j]==nums[j+1] and i<j:j-=1
                k+=1
    return triplet

# print(threesum([-1,0,1,2,-1,-4],0))
# print(threesum([0,1,1],0))
# print(threesum([0,0,0],0))
# print(threesum([2,2,2,2],6))
print(threesum([-2,0,0,2,2],0))