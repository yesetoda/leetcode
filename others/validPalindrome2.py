# class Solution:
#     def validPalindrome( s: str) -> bool:
#         s2 = list(s[::-1])
#         s1 = list(s)
#         if s1==s2:
#             return True
#         for i in range(len(s2)-1):
#             if s1[i] != s2[i]:
#                 del s1[i]
#                 s2 = s1[::-1]
#                 if s1 != s2:
#                     if s1[i] != s2[i]:
#                         del s2[i]
#                         s1 = s2[::-1]
#                         if s1 != s2:
#                             return False
#                         else: 
#                             return True
#                 else: 
#                     return True
            
#     s = "abc"
#     print(validPalindrome(s))

class Solution:
    def validPalindrome(s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                # Try removing i-th or j-th character
                return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]
            i += 1
            j -= 1
        return True

s = "aba"
print(Solution.validPalindrome(s))  # True

s = "abca"
print(Solution.validPalindrome(s))  # True

s = "abc"
print(Solution.validPalindrome(s))  # False