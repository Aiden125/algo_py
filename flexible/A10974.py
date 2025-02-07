from itertools import permutations

n = int(input())
arr = [x for x in range(1, n+1)]

for i in permutations(arr, n):
    print(*i)