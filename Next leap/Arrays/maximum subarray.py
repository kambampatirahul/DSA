'''Problem Description
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
'''

def maxSubarraySum(nums):
    currentMax = nums[0]
    globalMax = nums[0]

    for i in range(1, len(nums)):
        currentMax = max(nums[i], currentMax + nums[i])
        globalMax = max(globalMax, currentMax)

    return globalMax


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum = maxSubarraySum(nums)
print("Maximum Subarray Sum:", maxSum)

#This code is doen by using Kandens algorithm
#Here are the steps of Kadane's Algorithm:

# Initialize currentMax and globalMax to the first element of the array.
# Iterate through the array from the second element to the end.
# Update currentMax by adding the current element to the previous currentMax value.
# If currentMax becomes negative, reset it to zero.
# Update globalMax if currentMax is greater than globalMax.
# Repeat steps 3 to 5 for each element in the array.
# After iterating through all elements, globalMax will contain the maximum subarray sum.
