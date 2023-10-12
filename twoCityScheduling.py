class Solution:
    def twoCitySchedCost(costs: list[list[int]]) -> int:
        srt1 = sorted(costs)
        srt2  = sorted(costs,key = lambda x: x[1])
        print(srt1,srt2)
        print(min(srt1),min(srt2))
        for i in range(len(srt1)):
            min(srt1[i:])
    print(twoCitySchedCost(costs = [[10,20],[30,200],[400,50],[30,70]]))