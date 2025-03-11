import sys
import heapq

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pq = []
    for x in arr:
        heapq.heappush(pq, x)

    total = 0
    while len(pq) > 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        total += a + b
        heapq.heappush(pq, (a+b))
    print(total)
