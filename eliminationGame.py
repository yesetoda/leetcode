class Solution:
    def lastRemaining(n: int) -> int:
        x = [i for i in range(1,n+1)]
        while len(x)>1:
            leng = len(x)
            leng = leng//2 if leng%2==0 else  (leng+1)//2
            for i in range(leng):
                del x[i]
            print(x)
            x = x[::-1]
            
        return x[0]
    print(lastRemaining(44))
        