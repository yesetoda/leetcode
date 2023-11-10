# from collections import Counter

# def isIsomorphic( s, t):
#     a = Counter(s).values()
#     b = Counter(t).values()
#     a = list(a)
#     b = list(b)
#     print(a,b)
#     if a==b:
#         return True
#     else:
#         return False
# s = "bbbaaaba"
# t = "aaabbbba"
# print(isIsomorphic(s,t))


from collections import defaultdict


def isIsomorphic(s, t):
     def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if not s and not t:
            return True
        
        mapping = {}
        seen = set()
        counts = defaultdict(int)
        reverse_mapping = {}
        
        for i, char in enumerate(s):
            if char not in mapping:
                if t[i] in seen:
                    return False
                mapping[char] = t[i]
                counts[char] += 1
                seen.add(t[i])
                
                if t[i] in reverse_mapping:
                    return False
                else:
                    reverse_mapping[t[i]] = char
            elif mapping[char] != t[i]:
                return False
                
        # check both forward and reverse mappings for one-to-one
        if len(mapping) != len(reverse_mapping):
            return False
            
        return True