class Solution:
    def wordPattern(pattern: str, s: str) -> bool:
        p1 = pattern
        s1 = s.split()
        ptypes=0
        stypes=0
        d1 = {}
        if len(p1)!=len(s1):
            return False
        else:
            for i,j in zip(p1,s1):
                if j not in set(d1.values()):
                    print(j,d1.values())
                    stypes+=1
                if i in d1.keys():
                    if d1[i] != j:
                        return False
                else:
                    ptypes+=1
                    d1[i] = j
                print(j,set(d1.values()))
                print(ptypes,stypes)
            if ptypes!=stypes:
                    return False
        return True

pattern = "abba"
s ="dog cat cat dog"
print(Solution.wordPattern(pattern, s))