import re
class Solution:
    def isNumber(s):
        return re.match(r"-?\d*\.?\d+(?:[eE][+-]?\d+)?",s)
    print(isNumber("0e"))