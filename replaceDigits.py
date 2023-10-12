class Solution:
    def replaceDigits( s: str) -> str:
        s = [i for i in s[::]]
        for i in range(len(s)):
            if s[i].isdigit():
                s[i] =chr(ord(s[i-1])+int(s[i]))
        return "".join(s)
    s = "a1b2c3d4e"
    print(replaceDigits(s))