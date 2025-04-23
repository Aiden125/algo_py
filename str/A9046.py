n = int(input())

for _ in range(n):
    arr = [0] * 26
    str = input().replace(' ', '')
    max_value = 0
    for word in str:
        ask = ord(word)-97
        arr[ask] += 1
        max_value = max(arr[ask], max_value)
    count = 0
    index = -1
    for i in range(len(arr)):
        if arr[i] == max_value:
            count += 1
            index = i
    if count == 1:
        print(chr(index+97))
    else:
        print('?')