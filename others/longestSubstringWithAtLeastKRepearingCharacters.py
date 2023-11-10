# class Solution:
    # def longestSubstring( s: str, k: int) -> int:
    #     st = set(s)
    #     splt = []
    #     new = s
    #     for i in st:
    #         if s.count(i)<k:
    #             splt.append(i)
    #     print(splt)
    #     for i in splt:
    #             if i in s:
    #                 new = new.replace(i," ")
    #             print(new)
    #     print(new)
    #     mx = 0
    #     new_list = new.split()
    #     for i in new_list:
    #         longestSubstring(i)
    #         if len(i)>mx:
    #             mx = len(i)
    #     return mx
def method(s: str, k: int) -> int:
    if len(s) < k:
        return 0

    counter = {}
    for char in s:
        counter[char] = counter.get(char, 0) + 1

    for char, count in counter.items():
        if count < k:
            return max(method(substring, k) for substring in s.split(char))

    return len(s)

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return method(s, k)
print(longestSubstring( s = "aaabb", k = 3))