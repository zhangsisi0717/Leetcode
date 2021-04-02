from type_checking import *
def divide(self, dividend: int, divisor: int) -> int: ##https://leetcode.com/problems/divide-two-integers/

    if dividend < 0 and divisor > 0:
        sign = -1
    elif dividend > 0 and divisor < 0:
        sign = -1
    else:
        sign = 1

    x=[1]
    y=[abs(divisor)]
    re=0
    a=abs(dividend)
    while y[-1] <= a:
        y.append(y[-1]+y[-1])
        x.append(x[-1]+x[-1])

    for i in range(len(y)-1,-1,-1):
        if a>=y[i]:
            re += x[i]
            a -= y[i]

    re = re * sign
    if re < -2147483648 or re > 2147483647:
        return 2147483647

    return re





