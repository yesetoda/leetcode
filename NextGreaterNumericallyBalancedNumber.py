# # class Solution:
# #     def nextBeautifulNumber(self, n: int) -> int:
# #         chk = [1, 22, 122, 212, 221, 333, 1333, 3133, 3313, 4444, 14444, 22444, 24244, 24424, 24442, 22333, 23233, 23323, 23332, 55555, 155555, 515555, 551555, 555155, 555515, 555551, 224444, 242444, 244244, 244424, 244442, 422444, 424244, 424424, 424442, 442244, 442424, 442442, 444224, 444242, 444422, 666666, 7777777, 6666666, 7666666, 7676666, 7676766, 7676767, 7666767, 6667767, 6666677, 7666677, 7666767, 7766767, 7776667, 7777667, 7777677, 7777767, 7777776]
# #         for i in  chk:
# #             chk[i] = str(i)
# #         print(chk)
# #         for i in chk:
# #             if i>n:
# #                 return i

# # out = []
# # for i in range(1,8):
# #     out.append(int(str(i)*i))
# # new = out.copy()
# # for i in range(len(out)-1):
# #     for j in range(i+1,len(out)):
# #         x = int(str(out[i])+str(out[j]))
# #         if x<=10**6:
# #             new.append(x) 
# # new.sort()
# # print(new)
# x = [1, 22, 122, 212, 221, 333, 1333, 3133, 3313, 4444, 14444, 22444, 24244, 24424, 24442, 22333, 23233, 23323, 23332, 55555, 155555, 515555, 551555, 555155, 555515, 555551, 224444, 242444, 244244, 244424, 244442, 422444, 424244, 424424, 424442, 442244, 442424, 442442, 444224, 444242, 444422, 666666, 7777777, 6666666, 7666666, 7676666, 7676766, 7676767, 7666767, 6667767, 6666677, 7666677, 7666767, 7766767, 7776667, 7777667, 7777677, 7777767, 7777776]

# print(312233 in x)
import itertools

def generate_permutations():
    permutations = []
    for num in range(1, 1000001):
        digits = str(num)
        frequency = [digits.count(digit) for digit in digits]
        if frequency == [int(digit) for digit in digits]:
            perm = set(itertools.permutations(digits))
            permutations.extend(int(''.join(p)) for p in perm)
    permutations = list(set(permutations))  # Remove duplicates
    return permutations

permutation_list = generate_permutations()
print(permutation_list)
print(1224444 in permutation_list)