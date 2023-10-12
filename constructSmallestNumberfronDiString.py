class Solution:
    def smallestNumber(pattern: str) -> str:
        I = 0
        D = 0
        pattern+=" "
        out = []
        nums = [str(i) for i in range(1,10)]
        if pattern[0]=="I":
                I= 1
        else:
                D =1
        for i in range(len(pattern)-1):
            if pattern[i]== pattern[i+1] and pattern[i]=="I":
                I+=1
            elif pattern[i] != pattern[i+1] and pattern[i]=="I":
                print(I)
                I=0
                D = 1
                
            elif pattern[i]== pattern[i+1] and pattern[i]=="D":
                D+=1
            elif pattern[i]!= pattern[i+1] and pattern[i]=="D":
                print(D)
                I=1
                D = 0
    print(smallestNumber(pattern = "IIIDIDDDIII"))
                