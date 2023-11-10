class Solution:
    def findComplement(num: int) -> int:
        num1 = bin(num)[2:]
        num1 = num1.replace("1","!")
        num1 = num1.replace("0","1")
        num1 = num1.replace("!","0")
        return int(num1,2)
    num =5
    print(findComplement(num))