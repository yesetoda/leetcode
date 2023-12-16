t = int(input())
for _ in range(t):
    n = int(input())
    dif = abs(round((n/3))*3-n)
    # print(dif)
    if dif>=10:
        print("Second")
    else:
        if dif % 2 == 1:
            print("First")
        else:
            print("Second")