from time import perf_counter


travel = [1]
garbage = ["G","M"]
    
class Solution:
    def garbageCollection(garbage: list[str], travel: list[int]) -> int:
        last = {"P":0,"G":0,"M":0}
        cnt = {"P":0,"G":0,"M":0}
        for i in range(len(garbage)):
            for j in garbage[i]:
                cnt[j]+=1
                last[j] = i
        for i in range(1,len(travel)):
            travel[i] = travel[i-1]+travel[i]
        print(travel,last,cnt)
        m = travel[last["M"]-1]+cnt["M"] if last["M"]>0 else cnt["M"]
        g = travel[last["G"]-1]+cnt["G"] if last["G"]>0 else cnt["G"]
        p = travel[last["P"]-1]+cnt["P"] if last["P"]>0 else cnt["P"]
        return m+p+g
    a = perf_counter()
    print(garbageCollection(garbage, travel))
    b = perf_counter()
    print(b - a)
