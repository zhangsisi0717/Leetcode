class Solution:
    """
    explaination:
    step 1: keep track of largest index of each letter in the list as a dictionary "last_occurrence"
    step 2: create a set "seen" to keep track of chosen letter
    step 3: create a stack, and iterate the list "s", if stack is empty, then append the current letter,
    if cur_letter < stack[-1] and cur_index < last_occurrence[stack[-1]](means we could meet stack[-1] later, so remove stack[-1] would make the final string smaller): then stack.pop()
        Until (stack is emtpy) or (stack[-1]>cur_letter) or (stack[-1] will not occur later)

    return stack
    """
def removeDuplicateLetters(self, s) -> int:
    stack = []
    seen = set()
    last_occurrence = {c: i for i, c in enumerate(s)}
    for i, c in enumerate(s):
        if c not in seen:
            # if the last letter in our solution:
            #    1. exists
            #    2. is greater than c so removing it will make the string smaller
            #    3. it's not the last occurrence
            # we remove it from the solution to keep the solution optimal
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(c)
            stack.append(c)
    return ''.join(stack)
















