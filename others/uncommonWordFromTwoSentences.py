from collections import Counter

class Solution:
    def uncommonFromSentences(s1: str, s2: str) -> list[str]:
        both = s1+" "+s2
        both = both.split()
        freq = Counter(both)
        out = []
        for i in freq.keys():
            if freq[i]==1:
                out.append(i)
        return out
    s1 = "apple apple"
    s2 = "banana"
    print(uncommonFromSentences(s1, s2))