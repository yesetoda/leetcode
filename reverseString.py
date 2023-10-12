class Solution:
    def reverseString(s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s[::-1]
    s = ["h","e","l","l","o"]
    print(reverseString(s))