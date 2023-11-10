# class Solution:
#     def licenseKeyFormatting(s: str, k: int) -> str:
#         ch = s.replace("-", "").upper()[::-1]
#         out = ""
#         count=0
#         for i in range(len(ch)):
#             print(out)
#             prev =out
#             out = ch[i]
#             out+=prev
#             count+=1
#             if count==k:
#                 if  i+1<len(ch):
#                     out+="-"
#                     count=0
#         return out
    
class Solution:
    def licenseKeyFormatting(s: str, k: int) -> str:
        ch = s.replace("-", "").upper()[::-1]
        out = ""
        count = 0
        for i in range(len(ch)):
            out = ch[i] + out
            count += 1
            if count == k:
                if i + 1 < len(ch):
                    out = "-" + out
                    count = 0
        return out

s = "5F3Z-2e-9-w"
k = 3
print(Solution.licenseKeyFormatting(s, k))    
