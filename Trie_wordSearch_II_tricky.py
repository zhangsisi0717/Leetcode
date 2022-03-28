from collections import defaultdict
"""
step 1 : create a trie based on words

step 2 : iterate all the cells in boards, once boards[i][j] is a key of trie, we start "backtracking" from this cell using our created trie and append all the matched words to the final result 

NOTE: a small trick to speed up is to prune the trie once we have found the matched words
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = dict()
        for word in words: ##create a trie based on words
            cur = trie
            for letter in word:
                if letter not in cur:
                    cur[letter] = dict()

                cur = cur[letter]
            cur["end"] = word

        matchedWords=set()
        def backtracking(r, c, trie, visited):

            visited[r][c] = True
            letter = board[r][c]
            cur_trie = trie[letter]


            word_matched = cur_trie.pop("end", False)  ##check we have reached to the end of a word
            if word_matched:
                matchedWords.add(word_matched)

            for dr,dc in  [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if 0<=r+dr<len(board) and 0<=c+dc<len(board[0]) and not visited[r+dr][c+dc] and board[r+dr][c+dc] in cur_trie:
                    backtracking(r+dr, c+dc, cur_trie, visited)

            visited[r][c] = False
            if not cur_trie: ####once we have found the matched words, we no longer need to traverse it again, as a result, we prune it from the trie
                trie.pop(letter)


        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in trie: ##start backtracking whenever the board[r][c] in trie
                    backtracking(r, c, trie, visited)

        return matchedWords






