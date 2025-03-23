"""
20300 서강근육맨 문제
"""
import sys
input = sys.stdin.readline

n = int(input())
lists = list(map(int, input().split()))

odd = False
if len(lists) % 2 != 0:
    odd = True

lists.sort()

max_v = -1
left = 0
right = len(lists) - 1


if odd == True:
    right -= 1
    max_v = lists[len(lists) - 1]

while left < right:
    max_v = max(max_v, lists[left] + lists[right])
    left += 1
    right -= 1 
print(max_v)

"""
운동기구가 홀수일때는 가장 큰거 버리고 시작
운동기구가 짝수일때는 정렬해서 근손실이 가장 큰거, 작은거 더해주기
"""