class Solution:
    def findTheDifference( s: str, t: str) -> str:
        for i in t:
            if i not in s:
                return i
            else:
                idx = s.index(i)
                s =s[:idx]+s[idx+1:]
    s = "abcdeabcd" 
    t = "abdcdeabcd"
    print(findTheDifference(s,t))
            