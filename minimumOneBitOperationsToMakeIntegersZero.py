def op(x):
    if x=="0":
        return "1"
    return "1"
class Solution(object):
    
    def minimumOneBitOperations( n):
        num = [i for i in bin(n)[2:]]
        print(num)
        leng = len(num)
        vals = ["0","1"]
        while int("".join(num),2)!=0:
            print( int("".join(num),2),num)
            if num[0]=="1":
                num[0]="0"
            print("if",num)
            if leng>3:
                for i in range(2,leng):
                        if num[i-1]=="1" and int("".join(num[0:i-2]),2) ==0:
                            num[i] = op(num[i])
            print("after",num)
            break
            # else:
            #     for i in range(3,leng):
            #         print(int("".join(num[0:i-2]),2))
            #         if num[i-1]=="1" and int("".join(num[0:i-2]),2) ==0:
            #             num[i] = op(num[i])
            #         print(num)
            
        """
        :type n: int
        :rtype: int
        """
        return 0
    minimumOneBitOperations(7)
