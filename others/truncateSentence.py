class Solution:
    def truncateSentence(s: str, k: int) -> str:
        return " ".join(s.split()[:k])
    
    s = "chopper is not a tanuki"
    k = 5
    print(truncateSentence(s,k))