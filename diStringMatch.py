class Solution:
    def diStringMatch( s: str) -> list[int]:
        x = -1
        y = len(s)+1
        out = []
        for i in s:
            if i == "I":
                x+=1
                out.append(x)
            elif i == "D":
                y-=1
                out.append(y)
        for i in range(len(s)+1):
            print(i,i not in out)
            if i not in out:
                out.append(i)
        return out
    s = "IDID"
    print(diStringMatch(s))