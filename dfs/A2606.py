def dfs(arr, number, visited):
    visited[number] = True
    nodes = arr[number]
    for node in nodes:
        if visited[node] == False:
            dfs(arr, node, visited)

n = int(input())
m = int(input())
graph = [] * (n + 1)
visited = [False] * (n + 1)
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph(a).append(b)
    graph(b).append(a)