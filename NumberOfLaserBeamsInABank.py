class Solution(object):
    def numberOfBeams( bank):
        floors = []
        for i in bank:
            if "1" not in i:
                pass
            else:
                floors.append(i.count("1"))
        print(floors)
        floors = floors[::-1]
        if len(floors)<=1:
            out =  0
        else:
            out = 0
            for i in range(len(floors)-1):
                for j in range(floors[i]):
                    out+=floors[i+1]
                
        return out
    print(numberOfBeams(["011001","000000","010100","001000"]))
    
    """
        :type bank: List[str]
        :rtype: int
        """
        