"""
1541 잃어버린 괄호
마이너스로 split
+로 split해서 계산
"""
import sys
input = sys.stdin.readline

given = input()

split_str = given.split("-")

answer = 0
i = 0
for str in split_str:
    a = 0
    for x in str.split("+"):
        a += int(x)
    if i == 0:
        answer += a
    else:
        answer -= a
    i += 1
print(answer)

"""
split할때 첫 bunch 별도 계산이 필요한 경우 어떻게 처리할지
"""