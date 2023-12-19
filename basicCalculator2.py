class Solution:
    def calculate( s: str) -> int:
        s = s.replace(" ","")
        stack = []
        p1 =0
        p0 = 0
        #the multiplication and division part
        while p1<len(s):
            if s[p1] in '/':
                p1+=1
                p2 = p1
                while p2<len(s) and s[p2].isdigit():
                    p2+=1
                num2 = int(s[p1:p2])
                p1 = p2-1
                stack.append(int(stack.pop()//num2))
            elif s[p1] in '*':
                p1 +=1
                p2 = p1
                while p2<len(s) and s[p2].isdigit():
                    p2+=1
                num2 = int(s[p1:p2])
                p1 = p2-1
                stack.append(stack.pop()*num2)
            elif s[p1].isdigit():
                p2 = p1
                while p2<len(s) and s[p2].isdigit():
                    p2+=1
                stack.append(int(s[p1:p2]))
                p1=p2-1
            elif s[p1] in "+-":
                stack.append(s[p1])
            p1+=1
            # print(stack)
        p1 = 0
        if len(stack)==1:
            return stack[0]
        s = stack.copy()
        stack = [s[0]]
        
        #the addition and subtraction part
        while p1<len(s):
            if str(s[p1]) in "+-":
                num1 = stack.pop()
                p2 = p1
                while p2<len(s) and s[p2].isdigit():
                    p2+=1
                num2 = int(s[p1+1])
                # print(num1,num2)
                if str(s[p1]) in '+':
                    stack.append(num1+num2)
                elif str(s[p1]) in '-':
                    stack.append(num1-num2)
            p1+=1
        result = stack[0]
        result = -1*((-1*result)%(2**31)) if  result<0  else (result%(2**31-1)) 
        return  result
    v = calculate(s = "0-2147483647")
    print(v)
