n = int(input())

people_list = []

for i in range(n):
    people = list(map(int, input().split()))
    people_list.append(people)

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        if people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]:
            rank +=1
    print(rank, end=' ')        