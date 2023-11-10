class Solution:
    def numRescueBoats(people: list[int], limit: int) -> int:
        people.sort()
        st = 0
        en = len(people)
        saved = 0
        rescBoats = 0
        while st<en:
            if people[st] + people[en-1] <= limit:
                en -= 1
                st += 1
                saved+=2
                rescBoats+=1
            else:
                    saved+=1
                    en-=1
                    rescBoats+=1
        return rescBoats
    print(numRescueBoats(people = [3,5,3,4], limit = 5))
# from random import randint
# print([randint(1,200) for i in range(5*10**4)])