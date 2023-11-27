class Solution:

    def longestPalindrome(self, s):
        def help(i, j, s, n, ma, rs):
            if (i > n or j > n):
                return rs
            ss = s[i:j]
            if (ss == ss[::-1] and ma < len(ss)):
                ma = len(ss)
                rs.append(ss)

            help(i, j + 1, s, n, ma, rs)
            help(i+1, j, s, n, ma, rs)

        rs = []
        help(0, 1, s, len(s), 0, rs)
        return rs
s = Solution()
print(s.longestPalindrome('bab'))
