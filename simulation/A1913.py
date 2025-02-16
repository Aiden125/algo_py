n = int(input())
target_num = int(input())

arr = [0] * (n * n)

count = 0
idx = 0
repeatCount = 1
while count < n*n:
    for k in range(2):
        for repeat in range(repeatCount):
            if count >= n*n:
                break
            arr[count] = idx % 4
            count += 1
        idx += 1
    repeatCount += 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [[0] * n for x in range(n)]
start = int(n/2)

current_num = 1
i = start
j = start

answer = [0] * 2
current_index = 0

while current_num <= n*n:
    board[i][j] = current_num
    if target_num == current_num:
        answer[0] = i + 1
        answer[1] = j + 1
    i = i + dx[arr[current_index]]
    j = j + dy[arr[current_index]]
    current_num += 1
    current_index += 1

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j], end = ' ')
    print()
print(*answer)


