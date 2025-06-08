from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        curX, curY = q.popleft()
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if visited[nx][ny] or arr[nx][ny] == 0:
                continue
            q.append([nx, ny])
            visited[nx][ny] = True


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 위치
    arr = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    # 배추 심어진 위치
    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1

    answer = 0
    for x in range(N):
        for y in range(M):
            if not visited[x][y] and arr[x][y] == 1: 
                bfs(x, y)
                answer += 1

    print(answer)