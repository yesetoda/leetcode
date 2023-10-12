from random import randint
def minimumTotal(triangle):
    leng = len(triangle)
    print(triangle)
    for i in range(leng-2,-1,-1):
            for j in range(i+1):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]                
print("the output is ",minimumTotal([[ randint(-10**4, 10**4) for i in range(j)] for j in range(1,200)]))