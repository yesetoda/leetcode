from collections import Counter

class Solution:
    def customSortString(order: str, s: str) -> str:
        a = Counter(s)
        out = ""
        for i in order:
            if i in a:
                for j in range(a[i]):
                    out+=i
                del a[i]
        for i in a.keys():
            for j in range(a[i]):
                    out+=i
        return out
    print(customSortString(order = "cbafg", s = "abcd"))