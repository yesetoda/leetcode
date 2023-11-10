class Solution:
    def hammingDistance(x: int, y: int) -> int:
        num1 =bin(x)[:1:-1]
        num2 = bin(y)[:1:-1]
        hmd = 0
        ml = max(len(num1),len(num2))
        if len(num1) == ml:
            num2 +="0"*(ml-len(num2))
        elif len(num2) == ml:
            num1 +="0"*(ml-len(num1))        
        for i in range(ml):
            if num1[i]!= num2[i]:
                hmd+=1
        return hmd
    print(hammingDistance(1,3))
        