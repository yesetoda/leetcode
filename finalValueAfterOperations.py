class Solution:
    def finalValueAfterOperations( operations: list[str]) -> int:
        x = 0
        for i in operations:
            if "++" in i:
                x+=1
            elif "--" in i:
                x-=1
        return x
    operations =["X++","++X","--X","X--"]
    print(finalValueAfterOperations(operations))