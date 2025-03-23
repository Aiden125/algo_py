"""
21314 민겸 수
1. 최대값 -> M끼리 최대한 뭉치고 K랑 콜라보, 만약 k안만나면 1로 출력
2. 최소값 -> 다 별도 출력
"""
import sys
input = sys.stdin.readline

given = input()

maxV = ''
minV = ''
mCount = 0

ten = 10
for x in given:
    if x == 'M':
        mCount += 1
    elif x == 'K' and mCount == 0:
        maxV += '5'
        minV += '5'
    else:
        maxV += str(pow(ten, mCount - 1) * 50)
        minV += str(pow(ten, mCount - 1)) + '5'
        mCount = 0

if mCount != 0:
    minV += str(pow(ten, mCount - 1))
    for x in range(mCount):
        maxV += '1'

print(maxV)
print(minV)


"""
보류
"""