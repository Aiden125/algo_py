import sys
sys.setrecursionlimit(10**6)

dx = [-1,0,1,0]
dy = [0,1,0,-1]
m, n, k = map(int, input().split())

board = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

# 벽 표기
for i in range(k):
    sJ, sI, eJ, eI = map(int, input().split())
    for ii in range(sI, eI):
        for jj in range(sJ, eJ):
            board[ii][jj] = 1

def dfs(x, y):
    visited[x][y] = True
    count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if visited[nx][ny] or board[nx][ny] == 1:
            continue
        count += dfs(nx, ny)
    return count

answer = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0 and not visited[i][j]:
            count = dfs(i, j)
            answer.append(count)

print(len(answer))
answer.sort()
print(*answer)