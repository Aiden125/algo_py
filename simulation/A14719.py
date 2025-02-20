n, m = map(int, input().split())
arr = list(map(int, input().split()))

def getTotalSum(arr):
    left_index = 0
    right_index = 1

    min_v = 0
    total = 0
    sum_list = []
    while right_index < len(arr):
        left = arr[left_index]
        right = arr[right_index]

        if (left <= right) or (right_index == len(arr) - 1):
            min_v = min(left, right)
            for i in sum_list:
                total += min_v - i
            sum_list = []
            left_index = right_index
            right_index += 1
        elif left > right:
            sum_list.append(arr[right_index])
            right_index += 1
    return total

a = getTotalSum(arr)
arr.reverse()
b = getTotalSum(arr)
print(max(a, b))