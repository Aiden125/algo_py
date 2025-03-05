import heapq
import sys
input = sys.stdin.readline

n = int(input())
arr = []
rooms = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[0], x[1]))

for lecture in arr:
    start, end = lecture
    if rooms and rooms[0] <= start:
        heapq.heappop(rooms)
    heapq.heappush(rooms, end)
    
print(len(rooms))


"""
tc
5
0 40
5 5
5 10
5 15
15 30

--> 3
"""