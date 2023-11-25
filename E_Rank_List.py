n, k = map(int, input().split())
teams = []

for _ in range(n):
    solved_problems, penalty_time = map(int, input().split())
    teams.append((solved_problems, penalty_time))

teams.sort(key=lambda x: (-x[0], x[1]))  # Sort in descending order of solved problems and ascending order of penalty time

count = 1
same_place = 0
for i in range(1, n):
    if teams[i] == teams[k-1]:
        if teams[i] == teams[i-1]:
            same_place += 1
        else:
            count += same_place + 1
            same_place = 0
    else:
        break

print(count)