for i in range(int(input())):
    leng = int(input())
    x = list(map(int,input().split()))
    start= 0
    end = 0
    mx = 0
    sm  =0
    while start+1<leng:
        if x[start]%2==x[start+1]%2:
            # print("this si the values",start,end,x[end:start+1])
            sm = sum(x[end:start+1])
            mx = max(sm,mx)
            start+=1
            end = start
        else:
            start+=1

        if start==leng-1:
            sm = sum(x[end:start+1])
            mx = max(sm,mx)
            break
    print(mx)