#https://leetcode.com/problems/maximal-square/solution/
def maximalSquare(matrix):
    row = len(matrix)
    col = len(matrix[0])
    maxLength= [[0 for _ in range(col)] for _ in range(row)]
    re=0
    for i in range(row): ##update last col
        if matrix[i][-1] == 1:
            maxLength[i][-1] ==1
            re=1

    for j in range(col): ##update last row
        if matrix[-1][col] ==1:
            maxLength[-1][j] == 1
            re=1

    for c in range(col-2,-1,-1):
        for r in range(row-2,-1,-1):
            maxLength[r][c] = min(maxLength[r+1][c],maxLength[r][c+1],maxLength[r+1][c+1]) + 1
            if maxLength[r][c] >1:
                re = maxLength[r][c]

    return re*re






