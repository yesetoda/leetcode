# from collections import Counter
# class Solution:
#     def allCellsDistOrder( rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
#         out = Counter()
#         for i in range(rows):
#             for j in range(cols):
#                 out[(i,j)]=abs((rCenter-i))+abs((cCenter-j))
#         out = [list(i[0]) for i in out.most_common()[::-1]]
#         return out
#     print(allCellsDistOrder( rows = 2, cols = 3, rCenter = 0, cCenter = 1))
#         # for row in rows:
#         #     for col in cols:
from random import randint
x = [randint(start,end) for i in range(length)
print(x)