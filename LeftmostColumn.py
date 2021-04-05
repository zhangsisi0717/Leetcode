class BinaryMatrix(): ##https://leetcode.com/problems/leftmost-column-with-at-least-a-one/discuss/1106451/Simple-Binary-Search
    def __init__(self,m):
        self.m = m
    def get(self, row: int, col: int):
       return self.m[row][col]
    def dimensions(self):
        return [len(self.m),len(self.m[0])]

m = BinaryMatrix([[0,0],[0,1]])


class solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        lb,ub = 0,dim[1]-1
        Found = False
        while(lb<=ub):
            mid = lb + int((ub-lb) /2)
            for r in range(dim[0]):
                if binaryMatrix.get(r,mid) == 1:
                    Found= True
                    ub = mid-1
                    break
            else:
                lb = mid+1

        return lb if Found else -1


