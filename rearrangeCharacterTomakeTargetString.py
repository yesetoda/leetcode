import math
class Solution:
    def rearrangeCharacters( s: str, target: str) -> int:
        same = []
        l = [i for i in s]
        t = [i for i in target]
        l = [i for i in s]
        for i in target:
            for j in l[:]:
                if i == j:
                    same.append(i)
                    l.remove(j)
                    print(l)
                else:
                    print("pass")
        s = "".join(same)
        print(s)
        return math.floor(len(s)/len(target))
                    
                
            
    s = "ilovecodingonleetcode"
    target ="code"
    print(rearrangeCharacters(s,target))