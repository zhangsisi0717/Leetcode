class Solution:
    """
    binary search, force range: lb= 0,
                                lb= max(position)-min(position)
    mid = (lb + ub)//2

    if force=mid. we need to count if given force==mid, how many ball at most we can have,
    if number of balls >= m, then we should make the "lb of force" larger
    if number of balls < m, then we should make the "ub of force" lower
    """
def maxDistance(self, position: List[int], m: int) -> int:

    def count(force,position,m): ##count how many balls at most if the minimal distance >= "force"
        ans,curr=1,position[0]
        for x in position:
            if x-curr>=force:
                ans+=1
                if ans >= m:
                    return True
                curr=x
        else:
            return False

    position.sort()
    lb,ub=1,position[-1]-position[0] ##lb, ub of possible force is between "0" and "max(position)-min(position)""

    while lb < ub - 1:
        mid=(lb+ub)//2
        if count(mid,position, m):
            lb=mid
        else:
            ub=mid-1
    return ub if count(ub,position, m) else lb



