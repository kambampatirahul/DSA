class Solution:
    def canThreePartsEqualSum(arr):
      s = sum(arr)/3
      if s==int(s):
        c = 0
        su = 0
        for i in arr:
          su+=i
          if su==s:
            su=0
            c+=1
          if c==3:return True
      return False
    print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
    print(canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
    print(canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
    print(canThreePartsEqualSum([1,-1,1,1]))
    print(canThreePartsEqualSum([0,0,0,0]))