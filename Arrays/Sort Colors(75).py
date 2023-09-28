class Solution:
    def sortColors(nums):
        top,mid,high = 0,0,len(nums)-1
        while(mid<=high):
            if(nums[mid]==2):
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            elif(nums[mid]==1):
                mid+=1
            elif(nums[mid]==0):
                nums[mid], nums[top] = nums[top], nums[mid]
                mid += 1
                top += 1
        print(nums)
    sortColors([2,0,2,1,1,0])

# Dutch national flag algorithm
'''The Dutch National Flag Algorithm works by partitioning the input array into three sections: elements less than a given value (e.g., 0), elements equal to the given value (e.g., 1), and elements greater than the given value (e.g., 2). The goal is to arrange the elements in such a way that all 0s appear before all 1s, and all 1s appear before all 2s.

The algorithm maintains three pointers: low, mid, and high. These pointers divide the array into four regions:

Elements before the low pointer represent 0s.
Elements between the low and mid pointers represent 1s.
Elements after the high pointer represent 2s.
Elements between the mid and high pointers are unprocessed and need to be examined.
The algorithm iterates through the array and performs the following operations:

Initialize low and mid pointers to the start of the array (index 0) and high pointer to the end of the array (index n-1, where n is the length of the array).
Iterate while the mid pointer is less than or equal to the high pointer.
If the element at the mid pointer is 0, swap it with the element at the low pointer, and increment both the mid and low pointers.
If the element at the mid pointer is 1, increment only the mid pointer.
If the element at the mid pointer is 2, swap it with the element at the high pointer, and decrement the high pointer.
Repeat steps 2 to 5 until the mid pointer crosses the high pointer.
After the algorithm completes, the array will be sorted with all 0s appearing before all 1s, and all 1s appearing before all 2s.'''