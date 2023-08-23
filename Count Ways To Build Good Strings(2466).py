class Solution:
    def countGoodStrings(low, high, zero, one):
        dp = [1] + [0] * (high)
        mod = 10**9+7
        for end in range(1, high+1):
            if end>=zero:
                dp[end]+=dp[end-zero]
            if end>=one:
                dp[end]+=dp[end-one]
        return sum(dp[low:high+1])%mod
    print(countGoodStrings(2,3,1,2))