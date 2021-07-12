#https://leetcode.com/problems/cinema-seat-allocation/
def maxNumberOfFamilies(n: int, reservedSeats: List[List[int]]) -> int:
"""
IF {2,3,4,5} WORK:
    result +=1
    then if {6,7,8,9} work => result +=1
ELIF {4,5,6,7} WORK, then result +=1
ELIF {6,7,8,9} WORK, then result +=1
"""
    row_to_seats = dict()
    for i in reservedSeats:
        if i[0] in row_to_seats:
            row_to_seats[i[0]].add(i[1])
        else: row_to_seats[i[0]] = {i[1]}

    total = 0
    for r in row_to_seats.values():
        if len(r) > 6: continue
        count = 0
        if not r&{2,3,4,5}:
            count +=1
            if not r&{6,7,8,9}:
                count +=1
        elif not r&{4,5,6,7}:
            count +=1

        elif not r&{6,7,8,9}:
            count +=1

        total += count
    return total + (n-len(row_to_seats))*2