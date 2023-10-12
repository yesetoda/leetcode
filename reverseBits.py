# class Solution:
#     def reverseBits( n: int) -> int:
#         s = str(n)[::-1]
#         return int(s,2)
    # n = input()
    # print(reverseBits(n))


class Solution:
    def reverseBits(n: int) -> int:
        binary_str = bin(n)[2:].zfill(32)  # remove '0b' prefix and pad with zeros
        reversed_str = binary_str[::-1]
        return int(reversed_str, 2)
    n = input()
    print(reverseBits(n))