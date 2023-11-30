t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    operations = 0
    prefix_sum = 0
    min_prefix_sum = float('inf')

    for i in range(n):
        prefix_sum += arr[i]
        if i >= m:
            prefix_sum -= arr[i - m]
        if prefix_sum <= min_prefix_sum:
            min_prefix_sum = prefix_sum
            operations += 1

    print(operations)