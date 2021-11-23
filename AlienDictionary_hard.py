##https://leetcode.com/problems/alien-dictionary/
from collections import deque
def alienOrder(words):
    re = ""
    used= set()
    allset= set()
    queue = deque()
    for i in range(len(words)-1):
        queue.append((words[i],words[i+1]))
        for letter in words[i]:
            allset.add(letter)
    for letter in words[-1]:
        allset.add(letter)

    while(queue):
        cur = queue.popleft()
        print(cur)
        if (not cur[0]) or (not cur[1]):
            continue
        elif cur[0][0] != cur[1][0]:
            if cur[0][0] in used and cur[1][0] not in used:
                re += cur[1][0]
                used.add(cur[1][0])

            elif cur[0][0] not in used and cur[1][0] in used:
                re = cur[0][0] + re
                used.add(cur[0][0])

            elif cur[0][0] not in used and cur[1][0] not in used:
                re = re + cur[0][0] + cur[1][0]
                used.add(cur[0][0])
                used.add(cur[1][0])

            elif cur[0][0] in used and cur[1][0] in used:
                p,s=None,None
                for idx in range(len(re)):
                    if re[idx] ==cur[0][0]:
                        p = idx
                    elif re[idx] ==cur[1][0]:
                        s= idx
                if p>s:
                    return ""

        elif cur[0][0] == cur[1][0] and cur[0][0] in used:
            queue.append((cur[0][1:],cur[1][1:]))
        elif cur[0][0] == cur[1][0] and cur[0][0] not in used:
            re = re + cur[0][0]
            used.add(cur[0][0])
            queue.append((cur[0][1:],cur[1][1:]))

    if not re:
        return ""
    notused=""
    for letter in allset:
        if letter not in used:
            notused += letter
    re += notused

    return re