"""
1931 회의실 배정
"""
import sys
input = sys.stdin.readline

n = int(input())
lists = [list(map(int, input().split())) for _ in range(n)]

lists.sort(key=lambda x: (x[1], x[0]))

answer = 0
emptyTime = 0
for x in lists:
    start, end = x;
    if emptyTime <= start:
        answer += 1
        emptyTime = end
print(answer)


"""
2차원 배열 정렬하는 법
"""