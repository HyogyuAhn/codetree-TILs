n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def divideEvenNum(arr):
    for i in range(n):
        arr[i] = int(arr[i] / 2) if arr[i] % 2 == 0 else arr[i]

divideEvenNum(arr)
print(*(i for i in arr))