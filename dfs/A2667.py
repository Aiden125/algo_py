n = int(input())
board = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 0, 1,0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    visited[x][y] = True
    count = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny] == True or board[nx][ny] == 0:
            continue
        count += dfs(nx, ny)

    return count

answer = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0 and visited[i][j] == False:
            count = dfs(i, j)
            answer.append(count)
            
answer.sort()
print(len(answer))
for i in answer:
    print(i)