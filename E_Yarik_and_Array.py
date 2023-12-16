# for i in range(int(input())):
#     leng = int(input())
#     ls = list(map(int,input().split()))
#     mx = max(ls)
#     sm = ls[0]
#     for i in range(leng-1):
#         sm = 0
#         for j in range(i,leng):
#             if ls[j]%2!=ls[j-1]%2:
#                 sm+=ls[j]
#             else:
#                 sm =ls[j]
#             mx = max(mx,sm)
#     print(mx)
# # Read the number of test cases

for _ in range(int(input())):
    leng = int(input())
    ls = list(map(int, input().split()))

    mx = max(ls)
    sm = ls[0]
    parity = [num % 2 for num in ls]

    for i in range(leng - 1):
        sm = 0
        for j in range(i, leng):
            if parity[j] != parity[j - 1]:
                sm += ls[j]
            else:
                sm = ls[j]
            mx = max(mx, sm)

    print(mx)