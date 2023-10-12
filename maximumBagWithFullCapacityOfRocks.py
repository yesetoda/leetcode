from random import randint
class Solution:
    def maximumBags( capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        available= []
        for i in range(len(capacity)):
            available.append(capacity[i]-rocks[i])
        available.sort()
        count = 0
        for i in range(len(available)):
            if available[i]==0:
                count+=1
            else:
                if additionalRocks-available[i]>=0:
                    count+=1
                    additionalRocks-=available[i]
                else:
                    break
        return count
    capacity = [randint(1,10**9) for i in range(5*10)]
    print(maximumBags(capacity  = capacity, rocks = capacity[1:]+[capacity[0]-1], additionalRocks = 1))