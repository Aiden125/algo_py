n = int(input())

min_v = 0
start = max(int(n/100), 0)
for i in range(start, n):

    jSum = 0

    j_list = list(map(int, str(i)))
    jSum = sum(j_list)
    if n == (i + jSum):
        min_v = i
        break

print(min_v)