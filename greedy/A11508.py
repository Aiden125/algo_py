import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

total = 0
idx = 0
for x in arr:
    idx += 1
    if idx != 1 and idx % 3 == 0:
        continue
    total += x
print(total)