n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n - 1):
    m = i
    for j in range(i + 1, n):
        if arr[j] < arr[m]:
            m = j
    tmp = arr[i]
    arr[i] = arr[m]
    arr[m] = tmp

print(*arr)