from collections import defaultdict
from typing import List

def calcEquation(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    f = lambda: defaultdict(f)
    numer_to_deno = f()
    for idx in range(len(equations)):
        numer_to_deno[equations[idx][0]][equations[idx][1]] = values[idx]
        numer_to_deno[equations[idx][1]][equations[idx][0]] = 1/values[idx]


    def findDivision(num,deno,visited):
        if num not in numer_to_deno or num in visited: return False
        visited.add(num)
        if deno in numer_to_deno[num]:
            return numer_to_deno[num][deno]

        for i in numer_to_deno[num]:
            temp = findDivision(i,deno,visited)
            if temp != False:
                return numer_to_deno[num][i] * temp

        return False

    result = []
    for n,d in queries:
        re = findDivision(n,d,set())
        if re != False:
            result.append(re)
        else:
            result.append(-1.0)
    return result


equations=[["a","b"],["b","c"]]
values=[2.0,3.0]
queries=[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

calcEquation(equations, values, queries)








