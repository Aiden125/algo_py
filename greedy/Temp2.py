"""
11508 2+1세일 문제
"""
import sys
input = sys.stdin.readline

n = int(input())
lists = [int(input()) for _ in range(n)]

lists.sort(reverse=True)

answer = 0
count = 0
for x in lists:
    count += 1
    if count % 3 == 0:
        count = 0
        continue
    answer += x
print(answer)

"""
import sys.stdin.realine
lists comprehension으로 입력받는 방법
reverse 정렬하는 법
"""