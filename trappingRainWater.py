class Solution:
    def trap(height: list[int]) -> int:
        length = len(height)
        if length == 0:
            return 0
        left_max = [0] * length
        right_max = [0] * length
        left_max[0] = height[0]
        print(height)
        for i in range(1, length):
            left_max[i] = max(left_max[i-1], height[i])
        right_max[length-1] = height[length-1]
        for i in range(length-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        total = 0
        print(left_max)
        print(right_max)
        for i in range(length):
            water_level = min(left_max[i], right_max[i])
            trapped_water = water_level - height[i]
            total += trapped_water
            print(total)
        return total
    print(trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))
    
    
# from random import randint
# x = [randint(0,10000) for i in range(2*10**4)]
# print(x)