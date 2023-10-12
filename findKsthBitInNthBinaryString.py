def inv(s):
    x = ""
    for i in s:
        if i=="0":
            x+="1"
        else:
            x+="0"
    return x
class Solution:
    def findKthBit(n: int, k: int) -> str:
        s= ["0"]
        for i in range(1,n):
            s.append(s[i-1]+"1"+inv(s[i-1])[::-1])
        return s[n-1][k-1]
    print(findKthBit(n = 4, k = 11))