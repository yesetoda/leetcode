from random import choice

class Solution:
    def generateTheString( n: int) -> str:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if n%2 ==1:
            return choice(letters)*n
        else:
            a = choice(letters)
            del letters[letters.index(a)]
            return a*(n-1)+choice(letters)*1
    n = 2
    print(generateTheString(n))