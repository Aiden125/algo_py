n, m = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

# 간선 정보 입력
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# stack을 활용한 dfs
def dfs_stack(start):
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)

for i in range(1, n+1):
    if not visited[i]:
        dfs_stack(i)
        count += 1

print(count)