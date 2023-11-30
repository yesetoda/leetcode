class Solution:
    def firstUniqChar( s: str) -> int:
        out = []
        for i in s:
            if s.count(i)==1:
                return s.index(i)
        return -1
    print(firstUniqChar("aabb"))