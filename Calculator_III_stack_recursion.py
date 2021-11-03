##https://leetcode.com/problems/basic-calculator-iii/
##https://leetcode.com/problems/basic-calculator/
from type_checking import *

from collections import deque
def calculate_stack(s: str) -> int:
    """
    Using a stack + recursion to deal with the "()"
       2*(5+5*2)/3+(6/2+8)"
    we need : {temp_string = "", presign = "+ ",stack = []}
    when we meet idx = "(", we need call recursion(idx+1), which we return result inside  "()" and the idx of ")",
    we continue to use stack to calculate the result as calculator II

    if s is a number, then:
        temp_string += s (we have not finished reading this number)

    if s is in "+-*/", then we have finished reading this number, call operate(stack, presign, number) method
        if presign is "+", append number to stack directly
        if presign is "-", apppend (-1)*number to stack
        if presign is "*", topNumber = stack.pop(), then append (topNumber * number)
        if presign is "/", topNumber = stack.pop(), then append (topNumber / number)

    eventually sum the stack
    """

    #!!!!!!we need to add a new operator  "+" to the end of string, in case the ending string is ")", under that circumstance, it will not
    # operate the previous operations
    s = s + "+"
    def operate(stack,presign,num):
        if presign == "+":
            stack.append(num)

        elif presign == "-":
            stack.append(-num)

        elif presign == "*":
            stack.append(stack.pop()*num)

        elif presign == "/":
            stack.append(int(stack.pop()/num))

    def recursion(idx): ##return the result,and index of ")" starting from index i
        stack = []
        temp_num = ""
        presign ="+"
        while(idx<len(s)):
            if s[idx] == "(":
                temp_num,idx = recursion(idx+1)

            elif s[idx] == ")":
                operate(stack,presign,int(temp_num))
                return sum(stack),idx

            elif s[idx].isnumeric():
                temp_num += s[idx]

            elif s[idx] in "+-*/":
                if temp_num: ##for case "-2 + 1"
                    operate(stack,presign,int(temp_num))
                temp_num = ""
                presign = s[idx]

            idx +=1

        return sum(stack),idx

    return recursion(0)[0]


s = "2*(5+5*2)/3+(6/2+8)"
# s = "2*(5+5*2)/3"
calculate_stack(s)



















