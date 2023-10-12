class Solution:
    def findThePrefixCommonArray( A: list[int], B: list[int]) -> list[int]:
        out = []
        for i in range(len(A)):
            out.append( len(set(A[:i+1]).intersection(set(B[:i+1]))))
        return out
    print(findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]))