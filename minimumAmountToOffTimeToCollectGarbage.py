class Solution:
    def garbageCollection(garbage: list[str], travel: list[int]) -> int:
        G = garbage[0].count("G")
        M = garbage[0].count("M")
        P = garbage[0].count("P")
        for i in range(1,len(travel)+1):
            if "G" not in "".join(garbage[i:]):
                break
            else:
                G+=travel[i-1]
                if "G" in garbage[i]:
                    G+= garbage[i].count("G")        
        for i in range(1,len(travel)+1):
            if "M" not in "".join(garbage[i:]):
                break
            else:
                M+=travel[i-1]
                if "M" in garbage[i]:
                    M+=garbage[i].count("M")        
        for i in range(1,len(travel)+1):
            if "P" not in "".join(garbage[i:]):
                break
            else:
                P+=travel[i-1]
                if "P" in garbage[i]:
                    P+=garbage[i].count("P")
        return G+P+M
    print(garbageCollection( garbage = ["MMM","PGM","GP"], travel = [3,10]))
