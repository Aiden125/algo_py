x = int(input())
peoples = []

for _ in range(x):
    a, b = map(int, input().split())
    peoples.append([a, b])

answer = []
for i in peoples:
    rank = 1
    for j in peoples:
        if i!=j and i[0] < j[0] and i[1] < j[1]:
            rank += 1
    answer.append(rank)

for i in answer:
    print(i)
    