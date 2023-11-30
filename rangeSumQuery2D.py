class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        cols = len(matrix[0])
        rows = len(matrix)
        self.prefix = [[0 ]*(cols+1)  for j in range(rows+1)]
        self.matrix = matrix
        for col in range(cols):
            for row in range(rows):
                self.prefix[row+1][col+1] = self.prefix[row][col+1]+self.prefix[row+1][col]-self.prefix[row][col]+matrix[row][col]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1]-self.prefix[row1][col2+1]-self.prefix[row2+1][col1]+self.prefix[row1][col1]
        
matrix = [
[3, 0, 1, 4, 2],
[5, 6, 3, 2, 1],
[1, 2, 0, 1, 5],
[4, 1, 0, 1, 7],
[1, 0, 3, 0, 5]
]

numMatrix = NumMatrix(matrix)
result1 = numMatrix.sumRegion(2, 1, 4, 3)
result2 = numMatrix.sumRegion(1, 1, 2, 2)
result3 = numMatrix.sumRegion(1, 2, 2, 4)

print(result1)  # Output: 8
print(result2)  # Output: 11
print(result3)  # Output: 12
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)