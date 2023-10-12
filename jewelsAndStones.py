class Solution:
    def numJewelsInStones( jewels: str, stones: str) -> int:
        numberOfJewels  = 0
        for i in stones:
            if i in jewels:
                numberOfJewels +=1
        return numberOfJewels
    jewels = "z"
    stones = "ZZ"
    print(numJewelsInStones(jewels,stones))