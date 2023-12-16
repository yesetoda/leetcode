class Solution:
    def stoneGameII(piles: list[int]) -> int:
        m=1
        ind=0
        while ind<len(piles):
            print(ind)
            ind+=m
            m = max(min(2*m,len(piles)-1),m)
            ind+=m
    print(stoneGameII(piles = [1,2,3,4,5,100,1,2,3,2,4,5,67,4,56,56,4,35]))