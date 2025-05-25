import sys
sys.setrecursionlimit(10**6)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x, y, start):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visited[nx][ny] or start != board[nx][ny]:
            continue
        dfs(nx, ny, start)

# 일반적인 케이스
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, board[i][j])
            count += 1

print(count, end=' ')

# 적록색약 케이스(G==R)
count = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'
            
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, board[i][j])
            count += 1

print(count)