class Solution:
    def fullJustify(words, maxWidth):
        li = []
        lte,te = 0,[]
        for i in words:
            lei = len(i)
            if(lte+len(te)+lei<=maxWidth):
                te.append(i)
            else:
                if(len(te) == 1):
                    li.append(" ".join(te) + " " * (maxWidth - lte))
                else:
                    s = " "*int((maxWidth-lte)/(len(te)-1))
                    es = (maxWidth - lte) % (len(te) - 1)
                    li.append(s.join(te).replace(s,s+' ',es))
                te = []
                te.append(i)
                lte=0
            lte+=lei
        li.append(" ".join(te)+" "*(maxWidth-lte-(len(te)-1)))
        return li
    print(fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))
    print(fullJustify(["What","must","be","acknowledgment","shall","be"],16))
    print(fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20))