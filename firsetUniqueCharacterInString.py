from collections import Counter
class Solution:
    def firstUniqChar( s: str) -> int:
        freq  = Counter(s)
        ones = []
        for i in s:
            # print(i,freq[i])
            if freq[i]<2:
                ones.append(s.index(i))
        # print(ones)
        if len(ones)==0:
            return -1
        return min(ones)
        # print(s)
    s = "aabb"
    print(firstUniqChar(s))