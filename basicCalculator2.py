class Solution:
    def calculate(s: str) -> int:
        stack = []
        out = 0
        i = 0
        while i<len(s):
            if s[i].isdigit():
                stack.append(s[i])
                i+=1
            elif s[i]=="/":
                stack.append(int(stack.pop())//int(s[i+1]))
                i+=2
            elif s[i]=="*":
                stack.append(int(stack.pop())*int(s[i+1]))
                i+=2
            elif s[i]=="+":
                stack.append(int(stack.pop())+int(s[i+1]))
                i+=2
            elif s[i]=="-":
                stack.append(int(stack.pop())-int(s[i+1]))
                i+=2
            print(stack)
        return stack[0]
    print(calculate(s = "3+2*2"))
        