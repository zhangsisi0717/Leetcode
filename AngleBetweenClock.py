#https://leetcode.com/problems/angle-between-hands-of-a-clock/submissions/
def angleClock(hour: int, minutes: int) -> float:
    number_of_minutes = minutes // 5 ## number corresponding to the minute pointer
    extra_angle_of_minutes = (minutes % 5) * 6 ##mod*6 should be the extra degree we need to add
    angle = 30 * (minutes/60) ##if hour == 12, as long as minutes !=0, hour pointer does not point to the exact number,
                                # the extra angle should be 30 * (minutes/60)

    distance = 12-hour+number_of_minutes if hour>number_of_minutes else number_of_minutes-hour
    cw_angle = abs(distance * 30 + extra_angle_of_minutes - angle)
    """
    clockwise angle should be : abs((angle between number of hour pointer and minute pointer) + (extra angle of minutes) - (extra angle of hour)) 
    """
    return min(360-cw_angle,cw_angle)

