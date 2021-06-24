#https://leetcode.com/problems/sudoku-solver/
from collections import defaultdict
from collections import deque
import copy
"""
step 1: implement check available numbers of certain (r,c) given on current board
step 2: dfs method to search for valid result and return
"""
def solveSudoku(board: List[List[str]]) -> None:
    empty = deque([(i,j) for i in range(9) for j in range(9) if board[i][j]=="."])
    block_dic = defaultdict(set)
    for i in range(9):
        for j in range(9):
            block_dic[(i//3,j//3)].add((i,j))

    def availableNum(board,r,c):
        num_set = {str(i) for i in range(1,10)}
        for col in range(9):
            if col!=c and board[r][col] in num_set:
                num_set.remove(board[r][col])
        for row in range(9):
            if row!=r and board[row][c] in num_set:
                num_set.remove(board[row][c])
        for _r,_c in block_dic[(r//3,c//3)]:
            if (_r,_c) !=(r,c) and board[_r][_c] in num_set:
                num_set.remove(board[_r][_c])
        return num_set

    def recur(board,empty):
        if not empty:
            return board
        cur_r,cur_c = empty[0]
        avail_items=availableNum(board,cur_r,cur_c)
        if not avail_items: return False
        for val in avail_items:
            copy_empty = copy.deepcopy(empty)
            copy_empty.popleft()
            copy_b = copy.deepcopy(board)
            copy_b[cur_r][cur_c] = val
            re = recur(copy_b,copy_empty)
            if re:
                return re
        return False
    result_b = recur(board,empty)
    for i in range(9):
        for j in range(9):
            board[i][j] = result_b[i][j]
