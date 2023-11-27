class Solution:
    def subarraySum(nums, k):
        i=j=su=c=0
        if(len(nums)==1):
            if nums[0]==k:c+=1
        else:
            while(j<len(nums)):
                if(su<k):
                    su+=nums[j]
                    j+=1
                if(su==k):
                    c+=1
                    su += nums[j]
                    j+=1
                if(su>k):
                    while (su > k):
                        su -= nums[i]
                        i += 1
            if(su==k):c+=1
        return c

    # print(subarraySum([1,1,1],2))
    # print(subarraySum([1,2,3],3))
    # print(subarraySum([1],0))
    print(subarraySum([-1,-1,1],1))