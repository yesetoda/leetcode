from math import round 


for i in range(int(input())):
    x = int(input())
    distance = round(x/3)*3-x
    if distance%2==1:
        print("First")
    else:
        print("Second")