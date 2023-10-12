from math import floor
from collections import Counter
import math
class Solution:
    def percentageLetter( s: str, letter: str) -> int:
        freq = Counter(s)
        totalLetters = sum(freq.values())
        return int(math.floor(freq[letter]/totalLetters*100))
    s = "sgawtb"
    letter ="s"
    print(percentageLetter(s,letter))