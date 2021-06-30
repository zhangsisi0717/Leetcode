from collections import defaultdict
"""
https://leetcode.com/problems/battleships-in-a-board/
"""
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        result=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) in visited: continue
                if board[i][j] == "X":
                    result +=1
                    for col in range(j+1,len(board[0])):
                        visited.add((i,col))
                        if board[i][col] !="X":
                            break

                    for row in range(i+1,len(board)):
                        visited.add((row,j))
                        if board[row][j] !="X":
                            break
        return result
