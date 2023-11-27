'''
Problem Description
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''

def sortcolors(nums):
    s=m=0
    e=len(nums)-1
    while(m<e):
        if(nums[m]==0):
            nums[s],nums[m]=nums[m],nums[s]
            s+=1
            m+=1
        elif(nums[m]==2):
            nums[e],nums[m]=nums[m],nums[e]
            e-=1
        else:m+=1
    return nums

print(sortcolors([2,0,2,1,1,0]))

'''
1.Initialize low and mid pointers to the start of the array (index 0) and high pointer to the end of the array (index n-1, where n is the length of the array).
2.Iterate while the mid pointer is less than or equal to the high pointer.
3.If the element at the mid pointer is 0, swap it with the element at the low pointer, and increment both the mid and low pointers.
4.If the element at the mid pointer is 1, increment only the mid pointer.
5.If the element at the mid pointer is 2, swap it with the element at the high pointer, and decrement the high pointer.
6.Repeat steps 2 to 5 until the mid pointer crosses the high pointer.
'''