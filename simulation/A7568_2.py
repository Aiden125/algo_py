n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = []
current = 0
while current < n:
    rank = 1
    target_a, target_b = arr[current]
    for i in range(n):
        if current == i:
            continue
        a, b = arr[i]
        if target_a < a and target_b < b:
            rank += 1
    answer.append(rank)
    current += 1
print(*answer)