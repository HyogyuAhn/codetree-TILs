n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def changeNum(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]

changeNum(arr)
print(*arr)