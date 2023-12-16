class Solution:
    def brightsestPos( lights: list[list[int]] )-> int:
        lights.sort()
        n2 = sorted(lights,key =lambda x:x[1])
        mn = abs(lights[0][0]-lights[0][1]) if lights[0][0]-lights[0][1]<0 else 0
        print(mn)
        mx = [0]*((n2[-1][0]+n2[-1][1])-(lights[0][0]-lights[0][1])+2)
        for i in lights:
            mx[mn+i[0]-i[1]] += 1
            mx[mn+i[0]+1+i[1]] -= 1
            print(mx)
        from itertools import accumulate
        prefixsum = list(accumulate(mx))
        print(mx)
        print(prefixsum)
        print("the max is ",max(prefixsum),prefixsum.index(max(prefixsum))-mn)
    print(brightsestPos( lights = [[1,2]]))
            