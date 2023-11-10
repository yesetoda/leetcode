class Solution:
    def fib(n: int) -> int:
        result=1
        if n ==0:
            return 0
        else:
            return n-2 + n-1
    n= 4
    print(fib(n))