'''
Problem Description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''
def twosum(nums,t):
    di = {}
    for i in range(len(nums)):
        if(t-nums[i] in di):
            return [i,di[t-nums[i]]]
        else: di.setdefault(nums[i],i)

print("approach1:",twosum([2,7,11,15],9))
print("approach1:",twosum([3,2,4],6))
print("approach1:",twosum([3,3],6))

def approach2(nums,t):
    nums.sort()
    i=0
    j=len(nums)-1
    while(i<=j):
        temp = nums[i]+nums[j]
        if(temp>t):
            j-=1
        elif(temp<t):
            i+=1
        else:
            return [i,j]

# print("approach2:",approach2([2,7,11,15],9))
print("approach2:",approach2([3,2,4],6))
print("approach2:",approach2([3,3],6))
'''
Approach1: 
1.create a empty dict/map
2.iterate through length of the nums
3.check if substraction of target and nums[i] is in dict or map return index i and index substraction of target and nums[i]
4.if not there in map/dict add nums[i] in map/dict

Approach2:
1.sort the list
2.add 2 pointers one at start and one at end
3.add values at two pointers and store in temp variable
4.if temp is greater than target decrease end pointer
5.if temp is less than target increase start pointer
6.if equal return pointers
7.do steps 3-6 untill pointers cross each other

diff - dosen't return the proper indices but returns correct values (here we r returning indices
'''