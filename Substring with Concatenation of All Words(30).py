from collections import Counter
class Solution:
    def findSubstring(s, words):
        window_len = len(words)
        word_len = len(words[0])
        target_states = {}
        for w in words:
            target_states[w] = target_states.setdefault(w, 0) + 1

        idxs = []

        def slide(shift):
            states = {}
            counts = 0
            start = 0 + shift
            l = start
            while start + window_len * word_len <= len(s):
                reset = False
                while l - start < window_len * word_len:
                    word = s[l:l + word_len]
                    l += word_len
                    if word not in target_states:
                        start = l
                        counts = 0
                        states = {}
                        reset = True
                        break

                    states[word] = states.setdefault(word, 0) + 1
                    if states[word] > target_states[word]:
                        break
                    if states[word] == target_states[word]:
                        counts += 1
                if reset:
                    continue
                if counts == len(target_states):
                    idxs.append(start)

                w = s[start:start + word_len]
                if states[w] == target_states[w]:
                    counts -= 1
                states[w] -= 1
                start = start + word_len

        for n in range(word_len):
            slide(n)
        return idxs

    # print(findSubstring("barfoofoobarthefoobarman",["bar","foo","the"]))
    # print(findSubstring("aaa",["a","a"]))
    # print(findSubstring("foobarfoobar",["foo","bar"]))
    print(findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))


# def s(A,k,n):
#     for i in range(n):
#         if k> 0:
#             B = A[i:k+i+1]
#             m =max(B)
#             ind = B.index(m)+i
#             p = A.pop(ind)
#             A.insert(i,p)
#             k=k-(ind-i)
#     print(A)
#
# n = int(input())
# k = int(input())
# A = []
# for i in range(n):
#     A.append(int(input()))
# s(A,k,n)
# # s([1,2,3,4],2)
# # s([1,3,2,3],3)
# # s([1,3,2,4],2)
# # s([1,2,2,3,2,3],6)
# # s([4,2,1,3],2)
# # s([4,2,1,3],3)


# import re
#
# string = 'foobarfoobar'
# substring = 'foobar'
#
# indices = [match.start() for match in re.finditer(f'(?={substring})', string)]
# print(indices)  # Output: [0, 1]
