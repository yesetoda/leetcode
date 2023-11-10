from collections import Counter
class Solution:
    def countBits( n: int) -> list[int]:
        out = []
        for i in range(n+1):
            binaryrep = bin(i)
            freqDict = Counter(binaryrep)
            ones=freqDict["1"]
            out.append(ones)
        return out