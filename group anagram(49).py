class Solution:
    def groupAnagrams(strs):
        d = {}
        for i in range(len(strs)):
            t = "".join(sorted(strs[i]))
            if t in d.keys():
                d[t].append(strs[i])
            else:
                d[t] = [strs[i]]
        print(list(d.values()))

    groupAnagrams(["eat","tea","tan","ate","nat","bat"])