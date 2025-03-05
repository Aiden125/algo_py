import sys
input = sys.stdin.readline

n = int(input())
arr = []

for x in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))
# sorted_arr = sorted(arr, key=lambda x: (x[1], x[0]))

answer = 0
room_end_time = 0
for x in range(n):
    startT, endT = arr[x]
    if room_end_time <= startT:
        answer += 1
        room_end_time = endT

print(answer)