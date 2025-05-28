n = int(input())
arr = list(map(int, input().split()))
temp = [0] * n

def mergeSort(arr, temp, low, high):
    if low < high:
        mid = (low + high) // 2
        mergeSort(arr, temp, low, mid)
        mergeSort(arr, temp, mid + 1, high)
        merge(arr, temp, low, mid, high)

def merge(arr, temp, low, mid, high):
    i, j, k = low, mid + 1, low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= high:
        temp[k] = arr[j]
        j += 1
        k += 1

    for idx in range(low, high + 1):
        arr[idx] = temp[idx]

mergeSort(arr, temp, 0, n - 1)
print(*arr)