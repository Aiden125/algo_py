# 준현은 되는대로 사서 마지막날에 판다
# 성민은 3일 오르면 팔고 3일 내리면 산다

money = int(input())
arr = list(map(int, input().split()))

jh = [money, 0]
sm = [money, 0]
up_count = 0
down_count = 0
pre_price = -1
for i in range(0, len(arr)):
    x = arr[i]
    if x <= money:
        jh[1] += jh[0] // x
        jh[0] = jh[0] % x
    if pre_price != -1 and pre_price < x:
        up_count += 1
        down_count = 0
    elif pre_price != -1 and pre_price > x:
        down_count += 1
        up_count = 0
    else:
        down_count = 0
        up_count = 0
    if down_count == 3:
        down_count = 0
        sm[1] += sm[0] // x
        sm[0] = sm[0] % x
    if up_count == 3:
        up_count = 0
        sm[0] += (x * sm[1])
        sm[1] = 0
    pre_price = x

last = arr[len(arr)-1]
jh[0] += (jh[1] * last)
sm[0] += (sm[1] * last)
if jh[0] > sm[0]:
    print("BNP")
elif jh[0] < sm[0]:
    print("TIMING")
else:
    print("SAMESAME")
    