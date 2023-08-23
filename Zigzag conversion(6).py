class Solution:
    def convert(s, numRows):
        if(len(s)==1 or numRows == 1):
            return s
        else:
            res, j, k = '', 0, 0
            i = (2 * numRows) - 2
            while (k < numRows):
                if(k!=0 and k!=numRows-1):
                    while (j < len(s)):
                        res += s[j]
                        if(j+i-(2*k)<=len(s)-1):
                            res += s[j+i-(2*k)]
                        j += i
                else:
                    while (j < len(s)):
                        res += s[j]
                        j += i
                print(res)
                k += 1
                j = k
            return res
    print(convert("PAB",3))