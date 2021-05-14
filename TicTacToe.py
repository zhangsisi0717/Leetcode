##https://leetcode.com/problems/design-tic-tac-toe/submissions/
"""
Explain: in order to check if current player could win after adding A(row,col) to the board, we only need to
check the row,col, two diagonals that include A(row,col)
"""
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = [[None for i in range(n)] for j in range(n)]
        #self.largest = [0,0]
        self.n = n


    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player
        win = True
        for r in range(self.n):
            if self.board[r][col] != player:
                win = False
                break

        if not win:
            win = True
            for c in range(self.n):
                if self.board[row][c] != player:
                    win = False
                    break
        if not win and row == col:
            idx=0
            win=True
            while(idx<self.n):
                if self.board[idx][idx] != player:
                    win = False
                    break
                idx +=1
        if not win and row+col == self.n-1:
            idx=0
            win=True
            while(idx<self.n):
                if self.board[idx][self.n-1-idx] != player:
                    win = False
                    break
                idx +=1

        return player if win else 0






# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)