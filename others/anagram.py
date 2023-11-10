from collections import Counter
class Solution:
    def isAnagram( s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        # l= [i for i in (set(a.keys())|set(b.keys))]
        notanagram = 0
        for i in a.keys():
            if i not in b.keys():
                notanagram+=1
            if a[i]!= b[i]:
                notanagram+=1
        for i in b.keys():
            if i not in a.keys():
                notanagram+=1
        if notanagram>0:
            return False
        else:return True
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s,t))