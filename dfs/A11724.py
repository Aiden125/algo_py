def dfs(graph, node, visited):
    visited[node] = True
    next_nodes = graph[node]
    for next_node in next_nodes:
        if visited[next_node] == False:
            dfs(graph, next_node, visited)
# 입력받기
n, m = map(int, input().split()) # 정점 개수, 간선 개수

# 배열, 방문 배열, 연결요소 카운트
graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)
count = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 연결요소 for문 돌면서 dfs
for i in range(1, n+1):
    if visited[i] == False:
        count += 1
        dfs(graph, i, visited)

print(count)