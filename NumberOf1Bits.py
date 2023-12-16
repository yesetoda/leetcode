class Solution:
    def hammingWeight( n: int) -> int:
        return bin(n)[2:].count('1')
from collections import Counter
class Solution:
    def hammingWeight( n: int) -> int:
        return Counter(bin(n)[2:])["1"]

