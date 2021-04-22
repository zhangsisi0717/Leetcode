def topoSort(graph): #######topological sort:DFS version
    visited=set()
    unvisited={i for i in range(7)}
    def dfs(cur_node):
        # print(f"node={cur_node}")
        visited.add(cur_node)
        unvisited.remove(cur_node)
        if cur_node not in graph:
            # print(f"current_path={[[cur_node]]}")
            return [cur_node]

        temp_re=[]
        for node in graph[cur_node]:
            if node not in visited:
                temp_re += dfs(node)

        temp_re.append(cur_node)
        # print(f"current_path = {temp_re}")
        return temp_re

    nodes = [i for i in graph.keys()]
    final=[]
    for v in nodes:
        if v in unvisited:
            final += dfs(v)

    return final

topoSort(graph)

def alienOrder(words) -> str:
    wordgraph=dict()
    visited,temp_visited=dict(),dict()
    for i in range(len(words)-1):
        idx=0
        found=False
        while(idx<len(words[i]) or idx<len(words[i+1])):
            if idx<len(words[i]):
                visited[words[i][idx]] = visited.get(words[i][idx],False)
                temp_visited[words[i][idx]] = temp_visited.get(words[i][idx],False)
            if idx<len(words[i+1]):
                visited[words[i+1][idx]] = visited.get(words[i+1][idx],False)
                temp_visited[words[i+1][idx]] = temp_visited.get(words[i+1][idx],False)
            if idx<len(words[i]) and idx<len(words[i+1]) and words[i][idx] != words[i+1][idx] and not found:
                if words[i+1][idx] not in wordgraph:
                    wordgraph[words[i+1][idx]] = [words[i][idx]]
                else:
                    wordgraph[words[i+1][idx]].append(words[i][idx])

                found=True
            idx+=1
    print(wordgraph)
    print(visited)
    def dfs(cur_node):
        if visited[cur_node]:
            return ""
        if cur_node not in wordgraph:
            visited[cur_node] = True
            return cur_node
        if temp_visited[cur_node] == True:
            return False
        temp_visited[cur_node] = True
        temp_re=""
        for node in wordgraph[cur_node]:
            re = dfs(node)
            if re == False:
                return False
            else:
                temp_re += re
        temp_re += cur_node
        temp_visited[cur_node]=False
        visited[cur_node] = True
        return temp_re

    final=""
    for v in visited.keys():
        if not visited[v]:
            result = dfs(v)
            if not result:
                return ""
            else:
                final += result

    return final



words=["wrt","wrf","er","ett","rftt"]
words=["z","x","z"]
words=["ab","adc"]
alienOrder(words)