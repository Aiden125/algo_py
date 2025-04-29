arr = [list(input()) for _ in range(5)]

word = ''
for current_index in range(5):
    for a in arr:
        if len(a) > current_index:
            word += a[current_index]
print(word)