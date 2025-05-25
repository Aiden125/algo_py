import sys
sys.setrecursionlimit(10**6)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

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

def dfs2(x, y, start):
    visited2[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if visited2[nx][ny]:
            continue
        if (start == 'R' or start == 'G') and board[nx][ny] == 'B':
            continue
        elif start == 'B' and start != board[nx][ny]:
            continue
        dfs2(nx, ny, start)

# 적록색약은 R==G
count = 0
count2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, board[i][j])
            count += 1
        if not visited2[i][j]:
            dfs2(i, j, board[i][j])
            count2 += 1

print(count, end=' ')
print(count2)