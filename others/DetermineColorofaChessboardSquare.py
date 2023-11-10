class Solution:
    def squareIsWhite(coordinates: str) -> bool:
        if (ord(coordinates[0])%2 ==1 and int(coordinates[1])%2 ==1) or (ord(coordinates[0])%2 ==0 and int(coordinates[1])%2 ==0): 
            return False
        else: 
            return True
    coordinates = "c7"
    print(squareIsWhite(coordinates))