'''
Problem Description
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''

#approach 1
def singlenumber(nums):
    li = []
    for i in nums:
        if i in li:
            li.remove(i)
        else: li.append(i)
    return li[0]

print("approach1:",singlenumber([4,1,2,1,2]))

#approach 2
def approach2(nums):
    di = {}
    for i in nums:
        di[i]=di.setdefault(i,0)+1
    for i in di:
        if di[i] == 1:
            return di[i]

print("approach2:",approach2([4,1,2,1,2]))

'''
Approach 1:
1. create a new empty list
2. iterating through the nums list and check each element is there in new list
3. if element not there append it else remove it
4. return new list

Approach 2:
1.create a empty map or dictonary
2.iterate through nums list and count the number of different elements
3.iterate through map/dict check for the value having one as integer and return its key
'''