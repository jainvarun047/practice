#!usr/bin/python3

from collections import defaultdict


def minEdgeReversals(n: int, edges: list[list[int]]) -> list[int]:
    graph = defaultdict(list)

    for edge in edges:
        u = edge[0]
        v = edge[1]
        graph[u].append((v,0))
        graph[v].append((u,1))
    
    answer = [0] * n
    visited = [False] * n

    def dfs_initial(u):
        visited[u] = True
        total = 0
        for v,cost in graph[u]:
            if not visited[v]:
                total += cost + dfs_initial(v)
        return total
    
    answer[0] = dfs_initial(0)

    def dfs_re_root(u):
        visited[u] = True
        for v,cost in graph[u]:
            if not visited[v]:
                if cost == 0:
                    answer[v] = answer[u] + 1
                else:
                    answer[v] = answer[u] - 1
                dfs_re_root(v)
    
    visited = [False] * n
    dfs_re_root(0)

    return answer
