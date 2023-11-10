class Solution:
    def toHex(num: int) -> str:
        if num<0:
            a = ""
            b = ""
            x = bin(abs(num))[2:]
            print(len(x))
            if len(x)%32!=0:
                for j in range(32-len(x)%32):
                    a+="0"
                a +=x
            a+=x
            for i in a:
                if i=="0":
                    b+="1"
                else:
                    b+="0"
            print(b,int(b))
            return hex(int(b,2)+1)[2:]
        else:
            return hex(num)[2:]
    print(toHex(-1))