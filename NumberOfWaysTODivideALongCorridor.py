class Solution:
    def numberOfWays( corridor: str) -> int:
        print(len(corridor))
        print(corridor)
        cnt = 0
        found = False
        ind = 0
        out = 1
        inds = []
        for i in range(len(corridor)):
            if cnt==2:
                if not found:
                    found =True
                cnt = 0
            if corridor[i]=="S":
                cnt+=1
                out*=ind
                print("this is the value of the ind and out",i,ind),out
                ind = 0
            if found ==True and cnt==0:
                ind+=1
        if cnt%2!=0:
            print("there is no possible way")
        else:
            print(ind)
    print(numberOfWays( corridor = "PPSSPPSPSPPSPSPP"))