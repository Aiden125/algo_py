from collections import deque
import sys
input = sys.stdin.readline

# 8방향
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def bfs(x, y, arr, visited):
    visited[x][y] = True
    q = deque()
    q.append([x, y])

    while q:
        a, b = q.popleft()
        for a, b in dx, dy:
            nx = a + dx[i]
            ny = b + dy[i]
            if not (0<=nx<h and 0<=ny<w):
                continue
            if visited[nx][ny] or arr[nx][ny] == 0:
                continue
            q.append([nx, ny])
            visited[nx][ny] = True # q에 들어간순간 탐색대상이 되기 때문에 방문처리를 넣자마자 해주기

while(True):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == 1:
                bfs(i ,j, arr, visited)
                count += 1
    print(count)