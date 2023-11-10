class Solution:
    def splitNum( num: int) -> int:
        num = sorted(str(num))
        one,two  ="0","0"
        for i in range(len(num)):
            if i%2==0:
                one+= num[i]
            else:
                two+= num[i]
        print(one,two)
        return int(one)+int(two)
    print(splitNum(num = 9043294))