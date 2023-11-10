# # class Solution:
# #     def shiftingLetters( s: str, shifts: list[int]) -> str:
# #         alphabet = [" ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# #         x = [i for i in s]
# #         for i in range(len(shifts)):
# #             for j in range(i+1):
# #                 x[j]= alphabet[((alphabet.index(x[j])+shifts[i])%26)]
# #         return "".join(x)
# #     shiftingLetters( s = "abc", shifts = [3,5,9])
# from random import randint,choice
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# print([randint(0,10**5) for i in range(1000)])
# # print("".join([choice(alphabet) for i in range(1000)]))

# z= ' hteis'
# print(z

# x = "1skd"
# print(x[0].upper())

# from itertools import permutations
# print(list(permutations(input().split(),2)))
# a = set()
# b = set()

# from math import asin,pi
# print(asin(7.071/10)*360/(2*pi))
print(ord("$"),ord("€"))
print(chr(65509))
