#https://leetcode.com/problems/gas-station/

def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

    delta = [g - c for g, c in zip(gas, cost)]
    s = sum(delta)
    n = len(gas)
    """
    
    """

    # if s is negative, always infeasible
    if s < 0:
        return -1

    # after this, we can assume s >= 0

    t = 0  # gas remaining
    i = 0  # starting from station i
    j = 0  # just passed station j, currently at station j + 1 (mod n)

    while True:
        t += delta[j]  # gas remaining after passed station j and just arrived at j + 1
        if t < 0:
            t = 0
            i = j + 1
        # tried all stations, but failed
        if i == n:
            return -1

        # successfully reached end
        if j == n-1:
            return i

        j += 1