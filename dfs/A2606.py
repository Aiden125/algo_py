def dfs(arr, number, visited):
    visited[number] = True
    nodes = arr[number]
    for node in nodes:
        if visited[node] == False:
            dfs(arr, node, visited)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)] 
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)
print(visited.count(True) - 1)