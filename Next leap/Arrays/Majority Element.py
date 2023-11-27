'''
Problem Description
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''


def majority(nums):
    m = None
    count =0
    for i in nums:
        if count == 0:
            m = i
        count+=(1 if i==m else -1)
    return m

print("approach1:",majority([3,2,3]))


def approach2(nums):
    di = {}
    for i in nums:
        di[i]=di.setdefault(i,0)+1
    # return list(di.keys())[list(di.values()).index(max(list(di.values())))]  this also works
    return max(di.keys(), key=di.get)

print("approach2:",approach2([3,2,3]))

'''
Approach1:
1. 
'''