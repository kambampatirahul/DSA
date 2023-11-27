class Solution:
    def simplifyPath(path):
        li = path.split('/')
        p = []
        for i in li:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if len(p)>0:
                    p.pop()
            else:
                p.append(i)
        return '/'+"/".join(p)
    print(simplifyPath("/home/user/Documents/../Pictures"))