##https://leetcode.com/problems/basic-calculator-ii/
from type_checking import *
from collections import deque
def calculate_stack(s: str) -> int:
    """
    Using a stack
       (+)5+6*2/4-5/2*6
    temp_string = ""
    stack = []
    is s is a number, then:
        temp_string += s (we have not finished reading this number)

    if s is in "+-*/", then we have finished reading this number, call operate(stack, presign, number) method
        if presign is "+", append number to stack directly
        if presign is "-", apppend (-1)*number to stack
        if presign is "*", topNumber = stack.pop(), then append (topNumber * number)
        if presign is "/", topNumber = stack.pop(), then append (topNumber / number)

    eventually sum the stack
    """
    def operate(stack,presign,num):
        if presign == "+":
            stack.append(num)

        elif presign == "-":
            stack.append(-num)

        elif presign == "*":
            stack.append(stack.pop()*num)

        elif presign == "/":
            stack.append(int(stack.pop()/num))

    s = s.strip()
    temp_num = ""
    presign = "+"
    stack = deque([])
    for i in range(len(s)):
        if i == len(s)-1:
            temp_num += s[i]
            operate(stack,presign,int(temp_num))

        elif i < len(s)-1 and s[i].isnumeric():
            temp_num += s[i]

        elif i < len(s)-1  and s[i] in "+-*/":
            operate(stack,presign,int(temp_num))
            temp_num = ""
            presign = s[i]

    return sum(stack)


s= "3+2*2/4+7*9/2-6*5*5/4"
calculate_stack(s)

#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################

class SolutionTwo:
    """
    s = " 3 + 5*2/6 - 7*8/2"
    Recursion (s):
        if no operators in the string:
            return int(s)
        else:
            if there is "+" in the string: s' = s.split("+")
                for s in s', result += recursion(s) return result

            if no "+", then try s" = s.split("-"): for substring in s", result -= recursion(s)

            if no "+" and "-", then only "*"and "/" then iterate from 0 to end.. calculate the result and return

    """
    def calculate(self, s: str) -> int:
        def splitRecur(s,start):
            s = s.strip()
            if start<=0:
                plus = s.split("+")
                if len(plus)>1:
                    re = 0
                    for i in plus:
                        re += splitRecur(i,1)
                    return re
            if start <=1:
                minus = s.split("-")
                if len(minus)>1:
                    re =0
                    for idx in range(len(minus)):
                        if idx ==0:
                            re += splitRecur(minus[idx],2)
                        else:
                            re -= splitRecur(minus[idx],2)
                    return re

            if "*" in s or "/" in s:
                re = 1
                cur = ""
                operator = "*"
                for idx in range(0,len(s)):
                    if idx == len(s)-1:
                        cur += s[idx]
                        if operator == "*":
                            re = re * int(cur)
                        else:
                            re = int(re / int(cur))

                    elif (s[idx] == "*" or s[idx] == "/"):
                        if operator == "*":
                            re = re * int(cur)
                        else:
                            re = int(re / int(cur))
                        cur = ""
                        operator = s[idx]

                    elif s[idx] != "*" and s[idx] != "/" and s[idx]:
                        cur += s[idx]

                return re

            return int(s)

        return splitRecur(s,0)

