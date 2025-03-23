"""
14916 거스름돈문제
"""
n = int(input())

max_v = n // 5
i = max_v

while i>=0:
    reserve = n - (i * 5)
    if (reserve % 2) == 0:
        print(i + (reserve // 2))
        break
    i -= 1
    
if i == -1:
    print(i)