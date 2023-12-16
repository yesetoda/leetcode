t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the array
    a = list(map(int, input().split()))  # Elements of the array

    if sorted(a) == a:
        print(0)
        continue

    min_value = min(a)
    min_index = a.index(min_value)

    count = 0

    for i in range(min_index, n):
        if a[i] >= a[i - 1]:
            count += 1
        else:
            break

    if count == n - 1:
        print(count)
    else:
        print(-1)