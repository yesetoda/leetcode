class Solution(object):
    def carFleet(target, position, speed):
        ps = {position[i]:speed[i] for i in range(len(position))}
        print(ps)
        position.sort(reverse = True)
        print(position)
    carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])