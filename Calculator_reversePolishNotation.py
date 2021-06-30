from collections import deque
from typing import List
"""
implement by using stack
"""
def evalRPN(tokens: List[str]) -> int:
    stack=deque([])
    idx=0
    operator = {"+":lambda x,y:x+y,"-":lambda x,y:x-y,"*":lambda x,y:x*y,"/":lambda x,y: int(x/y)}
    result=0
    while(idx<len(tokens)):
        print(f"tokens[idx]={tokens[idx]}")
        if tokens[idx] in ("+-*/"):
            y = stack.pop()
            x = stack.pop()
            result += operator[tokens[idx]](x,y)

        else:
            stack.append(int(tokens[idx]))

        idx +=1

        return result
