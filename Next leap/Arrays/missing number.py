'''
Problem Description
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
'''

def missingnumber(nums):
    n = len(nums)
    totsum = int((n*(n+1))/2)
    return totsum - sum(nums)

print(missingnumber([3,0,1]))

'''
This is one type of solution 
Steps:
1. calculating the sum of whole numbers using the formula
2. calculating the sum of the given numbers in the list
3. doing the substraction gives us the result

But this approach will work only when the extra number is given as n+1

Approach 2:
1. sort the list
2. do any search operation
'''