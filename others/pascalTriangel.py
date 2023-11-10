# from itertools import combinations
from math import comb
class Solution:
    def generate(numRows):
        l = []
        m= [l*(i+1) for i in range(numRows)]
        for i in range(numRows):
            print("i-->",i)
            for j in range(i+1):
                m[i].append(comb(i, j))
                print("j-->",j)
                
        return m
    print(generate(6))