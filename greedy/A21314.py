given = input()

min_value = ''
max_value = ''

count = 0

for chunk in given:
    if chunk == 'M':
        count += 1
    else:
        if count == 0:
            min_value += '5'
            max_value += '5'
        else:
            min_value += str(10 ** (count - 1)) + '5'
            max_value += str(5 * (10 ** (count)))
            count = 0

if count != 0:
    min_value += str(10 ** (count - 1))
    max_value += ('1' * count)

print(max_value)
print(min_value)