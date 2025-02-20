m = int(input())

for five in range(m//5, -1, -1):
    answer = 0
    remain = m - (5 * five)
    if remain % 2 == 0:
        answer += five + (remain//2)
        print(answer)
        break
else:
    print(-1)
    