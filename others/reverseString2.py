class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        res = ''
        i = 0
        while i < n:
            if i + k <= n:
                res += s[i:i+k][::-1]
                res += s[i+k:i+2*k]
            else:
                res += s[i:][::-1]
            i += 2*k
        return res
    s = "abcdefg"
    k = 2
    print(reverseStr(s,k))
"""
The reverseStr method takes a string s and an integer k as inputs, 
and returns a new string where the first k characters for every 2k 
characters counting from the start of the string are reversed.

The method initializes an empty string res to store the result, 
and an integer variable i to keep track of the current position 
in the input string s. It also computes the length n of the input
string.

The method then enters a loop that iterates over every 2k characters
in the input string. For each iteration, it checks if there are at 
least k characters left in the string starting from the current position 
i. If there are, it reverses the first k characters using slicing and the
[::-1] notation, and appends them to the result string res. It then appends
the next k characters (or fewer if there are less than k characters left)
to res without reversing them.

If there are less than k characters left in the string starting from the 
current position i, the method simply reverses all of them and appends them
to res.

Finally, the method updates the position i to the next 2k characters in the
input string, and continues the loop until the end of the string is reached.
"""