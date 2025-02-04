n = int(input())

min_v = 0
start = max(1, n - (len(str(n)) * 9)) # 999의 경우를 생각해보자 각 자리수의 합은 (자리수*9)를 넘을 수 없다.

for i in range(start, n):
    j_list = list(map(int, str(i)))
    jSum = sum(j_list)
    if n == (i + jSum):
        min_v = i
        break

print(min_v)