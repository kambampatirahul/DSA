
class Solution:

    def search(pat, txt):
        dtxt = {}
        i = 0
        ltxt = len(txt)
        c = 0
        for j in range(ltxt):
            dtxt[txt[j]] = dtxt.setdefault(txt[j],0)+1
        ldtxt = len(dtxt)
        j = 0
        lpat = len(pat)
        while(j<lpat):
            tt = pat[i:j+1]
            if(j-i<ltxt):
                if(pat[j] in dtxt):
                    dtxt[pat[j]]-=1
                    if dtxt[pat[j]] == 0:
                        ldtxt -= 1
            elif(j-i==ltxt):
                if(ldtxt==0):c+=1
                if(pat[i] in dtxt):
                    if dtxt[pat[i]] == 0:
                        ldtxt += 1
                    dtxt[pat[i]] += 1
                i+=1
                if (j<lpat and pat[j] in dtxt):
                    dtxt[pat[j]] -= 1
                    if dtxt[pat[j]] == 0:
                        ldtxt -= 1
            j+=1
        if(ldtxt==0):c+=1
        return c
    print(search('forxxorfxdofr','for'))
