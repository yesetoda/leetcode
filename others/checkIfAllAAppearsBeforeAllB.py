class Solution:
    def checkString(s: str) -> bool:
        if "b" in s:
            firstB = s.index("b")
        if "a" in s:
            lastA = len(s)-s[::-1].index("a")-1
        else:
            return True
        print(firstB,lastA)
        if firstB<lastA:
            return False
        return True
    s = "bbb"
    print(checkString(s))