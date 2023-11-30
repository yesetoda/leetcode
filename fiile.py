def nastya_and_doors(n, doors):
    good = [0] * (n + 1)
    bad = [0] * (n + 1)

    for k in range(1, n + 1):
        for i in range(0, n, k):
            if doors[i] == 0:
                bad[k] += 1
            else:
                good[k] += 1

    possible_solutions = []
    for k in range(1, n + 1):
        if good[k] == bad[k]:
            possible_solutions.append(k)

    return min(possible_solutions)