class Solution:
    def isPalindrome( s: str) -> bool:
        s = s.lower()
        realString = ""
        for i in s:
            if i.isalnum():
                realString+=i
        print(realString)
        if realString == realString[::-1]:
            return True
        return False
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))