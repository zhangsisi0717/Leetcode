##https://leetcode.com/problems/01-matrix/submissions/
from collections import deque
"""
push all the "0s" to queue (because we know distance of "0"==0), and append all the neighbors of elements in queue one by one and update
the distance gradually, until the queue is empty

"""
def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    m = len(mat)
    n = len(mat[0])
    res = [[0 if mat[i][j] == 0 else -1 for j in range(n)] for i in range(m)]

    q = deque((i, j) for j in range(n) for i in range(m) if mat[i][j] == 0)
    while q:
        x, y = q.popleft()
        d = res[x][y]
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and res[nx][ny] == -1:
                res[nx][ny] = d + 1
                q.append((nx, ny))
    return res





