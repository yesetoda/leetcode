class Solution(object):
    def matrixBlockSum( mat, k):
        row = len(mat)
        col = len(mat[0])
        
        prefix_sum = [[0 for _ in range(col+1)] for _ in range(row+1)]
        
        # Compute prefix sum for each row
        for i in range(1, row+1):
            for j in range(1, col+1):
                prefix_sum[i][j] = prefix_sum[i][j-1] + mat[i-1][j-1]
        
        # Compute the matrix block sum
        out = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                r1 = max(i-k, 0)
                c1 = max(j-k, 0)
                r2 = min(i+k+1, row)
                c2 = min(j+k+1, col)
                out[i][j] = prefix_sum[r2][c2] - prefix_sum[r2][c1] - prefix_sum[r1][c2] + prefix_sum[r1][c1]
        
        return out

    print(matrixBlockSum(mat=[[1,2,3],[4,5,6],[7,8,9]], k=1))
