from collections import Counter
class Solution:
    def numberOfSubstrings( s: str) -> int:
        freq = Counter(s[:3])
        cnt = 1 if len(freq)==3 else 0
        print(freq)
        for i in range(3,len(s)):
            print(i)
            freq[s[i-3]]-=1
            freq[s[i]]+=1
            if freq[s[i-3]]==0:
                del freq[s[i-3]]
            if len(freq)==3:
                cnt+=1
            print(freq)
        print(cnt)
    numberOfSubstrings("abcdefabc")