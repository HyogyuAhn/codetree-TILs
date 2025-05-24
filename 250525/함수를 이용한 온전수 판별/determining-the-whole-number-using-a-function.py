a, b = map(int, input().split())

# Please write your code here.
def isPerfectNum(n):
    return n % 2 != 0 and str(n)[len(str(n)) - 1] != '5' and not (n % 3 == 0 and n % 9 != 0)
    
def countPerfNum(a, b):
    cnt = 0
    for i in range(a, b + 1):
        if isPerfectNum(i):
            cnt += 1
    return cnt

print(countPerfNum(a, b))