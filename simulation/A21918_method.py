"""
21918번 전구
"""
import sys
input = sys.stdin.readline

n, command = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

# i번째 전구 상태를 x로 변경
def first(arr, i, x):
    arr[i] = x

# l부터 r까지 상태를 변경
def second(arr, l, r):
    for idx in range(l, r+1):
        arr[idx] = (arr[idx] + 1) % 2

# l부터 r까지 끈다
def third(arr, l, r):
    for idx in range(l, r+1):
        arr[idx] = 0

# l부터 r까지 켠다
def fourth(arr, l, r):
    for idx in range(l, r+1):
        arr[idx] = 1

for _ in range(command):
    a, b, c = map(int, input().split())
    if a == 1:
        first(arr, b-1, c)
    elif a==2:
        second(arr, b-1, c-1)
    elif a==3:
        third(arr, b-1, c-1)
    else:
        fourth(arr, b-1, c-1)

print(*arr)