from itertools import combinations
abs = list(int(input()) for _ in range(9))

for x in combinations(abs, 7):
    if sum(x) == 100:
        for y in sorted(x):
            print(y)
        break