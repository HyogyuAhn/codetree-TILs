a, b = map(int, input().split())

# Please write your code here.
def isPrimeNum(n):
    isPrime = True
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break
    return isPrime

def sumIsEven(n):
    return sum(int(d) for d in str(n)) % 2 == 0

cnt = 0
for i in range(a, b + 1):
    if isPrimeNum(i) and sumIsEven(i):
        cnt += 1
print(cnt)