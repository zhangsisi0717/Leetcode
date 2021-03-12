from type_checking import *
class SurroundedRegion: #https://leetcode.com/problems/surrounded-regions/
    """
    1. detect borders and record the postion where border blocks are "O"
    2. Use BFS to find all the connected blocks with the border blocks O, and record all the connected blocks
    3. Replace blocks which are not connected with "X"

    """
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque
        numRows,numCols = len(board),len(board[0])
        borders,connected,visited=[],[],set()
        queue = deque([])
        for r in range(numRows):
            if board[r][0] == "O" and r !=0 and r != numRows-1:
                borders.append((r,0,"r"))
                visited.add((r,0))
            if board[r][numCols-1] =="O" and r !=0 and r != numRows-1:
                borders.append((r,numCols-1,"l"))
                visited.add((r,numCols-1))

        for c in range(1,numCols-1):
            if board[0][c] == "O":
                borders.append((0,c,"d"))
                visited.add((0,c))

            if board[numRows-1][c] == "O":
                borders.append((numRows-1,c,"u"))
                visited.add((numRows-1,c))

        for o in borders:
            connected.append((o[0],o[1]))
            queue.append(o)
            print(f"Current O: {o}")
            while queue:
                print(f"queue: {queue}")
                print(f"currentQueue_len: {len(queue)}")
                print("\n")
                cur = queue.popleft()
                if (len(cur)==3 and cur[2] == "r") or len(cur)==2:
                    if board[cur[0]][cur[1]+1] == "O" and (cur[0],cur[1]+1) not in visited:
                        visited.add((cur[0],cur[1]+1))
                        queue.append((cur[0],cur[1]+1))
                        connected.append((cur[0],cur[1]+1))

                if (len(cur)==3 and cur[2] == "l") or len(cur)==2:
                    if board[cur[0]][cur[1]-1] == "O" and (cur[0],cur[1]-1) not in visited:
                        visited.add((cur[0],cur[1]-1))
                        queue.append((cur[0],cur[1]-1))
                        connected.append((cur[0],cur[1]-1))

                if (len(cur)==3 and cur[2] == "u") or len(cur)==2:
                    if board[cur[0]-1][cur[1]] == "O" and (cur[0]-1,cur[1]) not in visited:
                        visited.add((cur[0]-1,cur[1]))
                        queue.append((cur[0]-1,cur[1]))
                        connected.append((cur[0]-1,cur[1]))

                if (len(cur)==3 and cur[2] == "d" ) or len(cur)==2:
                    if board[cur[0]+1][cur[1]] == "O" and (cur[0]+1,cur[1]) not in visited:
                        visited.add((cur[0]+1,cur[1]))
                        queue.append((cur[0]+1,cur[1]))
                        connected.append((cur[0]+1,cur[1]))

        for r in range(1,numRows-1):
            for c in range(1,numCols-1):
                if r!=0 and c!=0 and board[r][c] == "O" and (r,c) not in connected:
                    board[r][c] = "X"


        return board



test2=[["X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","X","X"],["O","O","O","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","X"],["O","O","X","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","X","O"],["O","O","O","O","O","X","O","O","O","O","X","O","O","O","O","O","X","O","O","X"],["X","O","O","O","X","O","O","O","O","O","X","O","X","O","X","O","X","O","X","O"],["O","O","O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","X","X","X","O","X","O","O","O","O","X","X","O","X","O","O","O"],["O","O","O","O","O","X","X","X","X","O","O","O","O","X","O","O","X","O","O","O"],["X","O","O","O","O","X","O","O","O","O","O","O","X","X","O","O","X","O","O","X"],["O","O","O","O","O","O","O","O","O","O","X","O","O","X","O","O","O","X","O","X"],["O","O","O","O","X","O","X","O","O","X","X","O","O","O","O","O","X","O","O","O"],["X","X","O","O","O","O","O","X","O","O","O","O","O","O","O","O","O","O","O","O"],["O","X","O","X","O","O","O","X","O","X","O","O","O","X","O","X","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","O","O","O","X","O","X","O"],["X","X","O","O","O","O","O","O","O","O","X","O","X","X","O","O","O","X","O","O"],["O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O","O"],["O","O","O","X","O","O","O","O","O","X","X","X","O","O","X","O","O","O","X","O"],["O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O","O"],["X","O","O","O","O","X","O","O","O","X","X","O","O","X","O","X","O","X","O","O"]]
b = SurroundedRegion()
b.solve(test2)







