class Solution:
    def maxUncrossedLines(nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        matrix = [[-1 for col in range(m)] for row in range(n)]

        def UL(nums1, nums2, n, m, matrix):
            if (m == 0 or n == 0):
                return 0
            if (matrix[n - 1][m - 1] != -1):
                return matrix[n-1][m-1]
            if (nums1[n - 1] == nums2[m - 1]):
                l = 1 + UL(nums1, nums2, n - 1, m - 1, matrix)
                matrix[n-1][m-1] = l
                return matrix[n-1][m-1]
            else:
                l1 = UL(nums1, nums2, n - 1, m, matrix)
                l2 = UL(nums1, nums2, n, m - 1, matrix)
                matrix[n-1][m-1] = max(l1, l2)
                return matrix[n-1][m-1]
        return UL(nums1, nums2, n, m, matrix)
    print(maxUncrossedLines([1,4,2],[1,2,4]))
    print(maxUncrossedLines([2,5,1,2,5],[10,5,2,1,5,2]))
    print(maxUncrossedLines([2,1],[1,2,1,8]))