from collections import Counter
class Solution:
    def topKFrequent(nums, k):
        res = []
        n = Counter(nums)
        val = list(n.values())
        key = list(n.keys())
        for i in range(k):
            ind = val.index(max(val))
            res.append(key[ind])
            val.pop(ind)
            key.pop(ind)
        return res
    print(topKFrequent([1,2],2))