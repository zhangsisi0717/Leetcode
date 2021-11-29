"""
https://leetcode.com/problems/word-search/
iterate row,col in the board, if board[row][col] == word, do a dfs to find if the word could be matched

TimeComplexity O (N*K) N is total number of blocks in the board, K is length of words

Need to pay attention: we need to revert visited state back each time after the recursion since we need to do a lot
 of dfs, see line 32!!!
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_row, n_col = len(board), len(board[0])
        visited = [[False for _ in range(n_col)] for _ in range(n_row)]

        def backtrack(row, col, word_to_be_matched, n_row,n_col):
            if len(word_to_be_matched) == 0:# has reached to the end of word that need to be matched
                return True
            if (row < 0 or row >= n_row or col < 0 or col >= n_col) or visited[row][col]:
                return False

            if board[row][col] != word_to_be_matched[0]:
                return False


            visited[row][col] = True #mark the (row,col) as visited

            matched = False
            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:# explore the 4 neighbor directions
                matched = backtrack(row + rowOffset, col + colOffset, word_to_be_matched[1:],n_row,n_col)
                if matched:
                    break

            visited[row][col] = False ##revert back to unvisited

            return matched

        for row in range(n_row):
            for col in range(n_col):
                if board[row][col]== word[0] and backtrack(row, col, word,n_row,n_col):
                    return True

        # no match found after all exploration
        return False