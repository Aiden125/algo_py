from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(node):
    print(node, end=' ')
    visited[node] = True
    nexts = arr[node]
    nexts.sort()
    for next in nexts:
        if not visited[next]:
            dfs(next)

def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = True

    while q:
        current = q.popleft()
        print(current, end=' ')
        nexts = arr[current]
        nexts.sort()
        for next in nexts:
            if not visited[next]:
                q.append(next)
                visited[next] = True


# graph 완성
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(v)
visited = [False] * (n+1)
print()
bfs(v)