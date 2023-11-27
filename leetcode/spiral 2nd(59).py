class Solution:
    def generateMatrix(n):
        rt,lt,rb,lb,i = n-1,0,n-1,0,1
        res=[[0 for col in range(n)] for row in range(n)]
        while(lt<=rb and lb<=rt):
            t=lt
            while(t<rt+1):
                res[lt][t]=i
                i+=1
                t+=1
            lt+=1
            t=lt
            while(t<rb+1):
                res[t][rt]=i
                i+=1
                t+=1
            rt-=1
            t=rt
            while(t>lb-1):
                res[rb][t]=i
                i+=1
                t-=1
            rb-=1
            t=rb
            while(t>lt-1):
                res[t][lb]=i
                i+=1
                t-=1
            lb+=1
        print(res)
    generateMatrix(4)