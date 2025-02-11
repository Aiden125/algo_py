# 입력
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 함수
def light(arr, o, a, b):
    # 1번 a전구 상태 b로 변경
    # 2번 a~b 전구 상태 변경
    # 3번 a~b 전구 끄기
    # 4번 a~b 전구 켜기
    if o == 1:
        arr[a-1] = b
    elif o == 2:
        for i in range(a-1, b):
            arr[i] = 1 - arr[i]
    elif o == 3:
        for i in range(a-1, b):
            arr[i] = 0
    elif o == 4:
        for i in range(a-1, b):
            arr[i] = 1

for i in range(m):
    o, a, b = map(int, input().split())
    light(arr, o, a, b)
print(*arr)
