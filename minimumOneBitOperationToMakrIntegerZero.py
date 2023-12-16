from time import sleep
def change_bit(bit):
    return 1 if bit==0 else 0
class Solution:
    def minimumOneBitOperations( n: int) -> int:
        bn = [int(i) for i in bin(n)[2:]]
        print(bn)
        ind = 0
        while sum(bn)!=0:
            if bn[ind-1]==1 and sum(bn[max(ind-2,0):])==0:
                bn[ind] = change_bit(bn[ind-1])
            else:
                bn[-1] = change_bit(bn[-1])
            if bn[ind]==0:
                ind+=1
            print(bn)
            sleep(1)
    print(minimumOneBitOperations(n = 13))
# print(int("1101",2))