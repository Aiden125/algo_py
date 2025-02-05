from itertools import combinations

# 조합을 만드는케이스라 visited가 아닌 start가 필요하다. 나보다 작은애를 검사할 필요가 없다.

n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

def find(start, sum_value):
    global count

    if sum_value == s and start != 0:
        count += 1
    
    for i in range(start, n):
        find(i + 1, sum_value + arr[i])

find(0, 0)
print(count)