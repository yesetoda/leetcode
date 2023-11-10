class Solution:
    def addDigits(num: int) -> int:
        result = 0
        while len(str(num)) != 1:
            for i in str(num):
                result += int(i)
            num = result
            result = 0
        return num

print(Solution.addDigits(38))