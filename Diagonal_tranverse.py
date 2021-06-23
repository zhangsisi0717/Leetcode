from typing import List
class Solution:
    """
    https://leetcode.com/problems/diagonal-traverse/
     simply and plainly does what the problem statement asks us to do.
     just need to determine when need to change the direction
    """
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = [mat[0][0]]
        i,j = 0,0
        num_r,num_c = len(mat),len(mat[0])
        cur_dir = 0
        off_set = [(-1,1),(1,-1)]
        while (i,j) != (num_r-1,num_c-1):
            if i == num_r-1 and cur_dir == 1:
                j += 1
                cur_dir =0

            elif j==num_c-1 and cur_dir == 0:
                i+=1
                cur_dir =1

            else:
                i,j = i+off_set[cur_dir][0], j+off_set[cur_dir][1]
                if i<0:
                    cur_dir = 1
                elif j<0:
                    j=0
                    cur_dir = 0
            result.append(mat[i][j])

        return result