for i in range(int(input())):
    n,k = map(int,input().split())
    data = list(map(int,input().split()))
    good = [0] * (n + 1)
    bad = [0] * (n + 1)

    for k in range(1, n + 1):
        for i in range(0, n, k):
            if data[i] == 0:
                bad[k] += 1
            else:
                good[k] += 1
    print(good,bad)
    possible_solutions = []
    for k in range(1, n + 1):
        if good[k] == bad[k]:
            possible_solutions.append(k)
    print(min(possible_solutions))