class Solution:
    def selfDividingNumbers( left: int, right: int) -> list[int]:
        output =[]
        for i in range(left,right+1):
            if "0" in str(i):
                pass
            else:
                notselfdiv = 0
                for j in str(i):
                    if i%int(j)!=0:
                        notselfdiv +=1
                if notselfdiv == 0:
                    output.append(i)
        return output
    left = 1
    right = 22
    print(selfDividingNumbers(left,right))