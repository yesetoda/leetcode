def baser(x, num):
    out = ""
    pw = 0
    while num != 0:
        rem = num % x
        if rem != 0:
            num -= rem
            out += str(rem)
        else:
            num //= x
            out += "0"
        pw += 1
        if num == 0:
            break
    return out[::-1]

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n):
            if baser(i, n) != baser(i, n)[::-1]:
                return False
        return True
    print(isStrictlyPalindromic(int(input())))
