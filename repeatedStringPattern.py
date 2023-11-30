class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        freq = Counter(s)
        out = []
        for i in freq.values():
            out.append(i)
        for i in range(1,len(out)):
            if out[i-1]%2!=out[i]%2:
                return False
        return True
    