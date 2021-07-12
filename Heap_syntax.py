def validTicTacToe(board: List[str]) -> bool:
    X_same_col = {i:0 for i in range(3)}
    X_same_row = {i:0 for i in range(3)}
    X_diagonal = {"l":0,"r":0}

    O_same_col = {i:0 for i in range(3)}
    O_same_row = {i:0 for i in range(3)}
    O_diagonal = {"l":0,"r":0}

    type_to_count = {"X":0,"O":0}
    type_to_block = {"X":{0:X_same_col,1:X_same_row,2:X_diagonal},
                     "O":{0:Y_same_col,1:Y_same_row,2:Y_diagonal}

    win = {"X": False,"O":False}
    for r in range(3):
        for c in range(3):
    if not board[r][c]:
        s = board[r][c]
    type_to_count[s] +=1
    type_to_block[s][0]+=1
    type_to_block[s][1]+=1
    if i == j:type_to_block[s][2]["r"]+=1
    if i+j ==2: type_to_block[s][2]["l"]+=1
    if type_to_count[s]>=3 or type_to_block[s][1]>=3 or type_to_block[s][2]["r"]>=3 or type_to_block[s][2]["l"]>=3:
        win[s] = True
    if type_to_count["X"] - type_to_count["O"] > 1: return False
    if type_to_count["O"] > type_to_count["X"]: return False
    if type_to_count["O"]  == type_to_count["X"]:
        if win["X"]: return False

    if type_to_count["X"] - type_to_count["O"] == 1 and win["O"]: return False
    return True





















# from typing import List
# def validTicTacToe(board: List[str]) -> bool:
#     non_visited = set([(i,j) for i in range(3) for j in range(3)])
#     letter_to_count  = {"X":0,"O":0}
#     def ifwin(type,r,c,count,non_visited):
#         print(r,c,count,type)
#         if count == 3:
#             print(f"r={r},c={c},return 1")
#             return True
#
#         non_visited.remove((r,c))
#         letter_to_count[board[r][c]] +=1
#         count_win = 0
#         for i in range(r-1,r+2):
#             for j in range(c-1,c+2):
#                 print(f"i={i},j={j}")
#                 if 0<=i<3 and 0<=j<3 and board[i][j] == type and (i,j) != (r,c) and (i,j) in non_visited:
#                     count_win += ifwin(type,i,j,count+1,non_visited)
#
#         print(f"r={r},c={c},return {count_win}")
#         return count_win
#
#
# board = ["XXX","X  ","XOO"]
# non_visited = set([(i,j) for i in range(3) for j in range(3)])
# ifwin("X",0,0,1,non_visited)





False
