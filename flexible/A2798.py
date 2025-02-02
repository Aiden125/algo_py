import itertools

a, b = map(int, input().split())
cards = list(map(int, input().split()))

max_value = -999

for x in itertools.combinations(cards, 3):
    current_sum = sum(x)
    if current_sum <= b and max_value < current_sum:
        max_value = max(current_sum, max_value)
print(max_value)