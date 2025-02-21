n = int(input())
arr = list(map(int, input().split()))

arr.sort()

left = 0
right = len(arr)-1

maxV = -1
while left <= right:
    if left != right:
        maxV = max(arr[left] + arr[right], maxV)
    left += 1
    right -= 1
print(maxV)