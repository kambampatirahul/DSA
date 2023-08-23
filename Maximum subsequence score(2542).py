class Solution:
    def maxScore(nums1, nums2, k):
        h = []
        total = 0
        res = 0
        print(sorted(zip(nums2,nums1),reverse = True))
        for min_n2, n1 in sorted(zip(nums2,nums1),reverse = True):
            if len(h) == k:
                total =total - heapq.heappop(h)
            total +=n1
            heapq.heappush(h,n1)
            if len(h) == k:
                res = max(res, total * min_n2)

        print(res)
    maxScore([1,3,3,2],[2,1,3,4],4)