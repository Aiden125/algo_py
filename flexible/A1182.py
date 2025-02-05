from itertools import combinations
import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
for i in range(1, n+1):
    for j in combinations(arr, i):
        if s == sum(j):
            count += 1

print(count)