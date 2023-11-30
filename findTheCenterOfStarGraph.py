class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        mx = list(map(set,edges))
        x = mx[0]
        for i in range(1,len(edges)):
            x = x.intersection(mx[i])
        return x