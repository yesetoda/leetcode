class Solution:
    def convertToBase7( num: int) -> str:
        s = ""
        if num<0:
            num = abs(num)
            while num>=7:
                s+=str(num%7)
                num = num//7
            s = s+str(num)
            s = "-"+s[::-1]
        else:
            while num>=7:
                s+=str(num%7)
                num = num//7
            s = s+str(num)
            s = s[::-1]
        return s
    print(convertToBase7(-7))
