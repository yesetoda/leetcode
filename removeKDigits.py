
class Solution:
    def removeKdigits(num: str, k: int) -> str:
        for i in range(k):
            num = str(min(int(num[0]),int(num[1])))+num[2:]
        return num
        
