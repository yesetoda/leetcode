class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Reverse the input strings
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Initialize variables
        carry = 0
        result = []
        
        # Add the digits of the two numbers
        for i in range(max(len(num1), len(num2))):
            digit1 = int(num1[i]) if i < len(num1) else 0
            digit2 = int(num2[i]) if i < len(num2) else 0
            digit_sum = digit1 + digit2 + carry
            carry = digit_sum // 10
            result.append(str(digit_sum % 10))
        
        # Add the final carry, if any
        if carry:
            result.append(str(carry))
        
        # Reverse the result and return it as a string
        return ''.join(result[::-1])