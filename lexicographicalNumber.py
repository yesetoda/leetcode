class Solution:
    def lexicalOrder(n: int) -> list[int]:
        x = [f"{i}" for i in range(1,n+1)]
        return list(map(int,sorted(x)))
    print(lexicalOrder(2))