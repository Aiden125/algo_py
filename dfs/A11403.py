import sys
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

# graph 연결
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j] == 1:
            graph[i].append(j)

# dfs 탐색
def dfs(start, node):
    visited[start][node] = 1
    nextNodes = graph[node]
    for next in nextNodes:
        if next == start: # cyle 마무리
            visited[start][next] = 1
            continue
        if visited[start][next]: # 이미 돈 cycle
            continue
        dfs(start, next)

# graph 순환
for i in range(n):
    arr = graph[i]
    for node in arr:
        dfs(i, node)

for v in visited:
    print(*v)