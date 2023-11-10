class Solution:
    def maximumPopulation( logs: list[list[int]]) -> int:
        popu = []
        st,en = 2050,1950
        for i in logs:
            if i[0]<st:
                st=i[0]
            if i[1]>en:
                en=i[1]
        mx = 0
        for i in range(st,en+1):
            people = 0
            for y in logs:
                if y[0]<=i and y[1]>i:
                    people+=1
            if people>mx:
                mx=people
            popu.append([i,people])
        for i in popu:
                if i[1]==mx:
                    return i[0]
    print(maximumPopulation(logs = [[1950,1961],[1960,1971],[1970,1981]]))