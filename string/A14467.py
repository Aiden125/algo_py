n = int(input())
arr = [-1] * 11

count = 0
for i in range(n):
    a,b = map(int, input().split())
    if arr[a] != -1 and arr[a] != b:
        count += 1
    arr[a] = b
print(count)