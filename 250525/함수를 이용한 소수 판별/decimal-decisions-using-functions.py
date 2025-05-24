a, b = map(int, input().split())

# Please write your code here.
def isPrimeNum(n):
    isPrime = True
    for i in range(2, n):
        if n % i == 0:
            isPrime = False
            break
    return isPrime


def sumPrimeNum(a, b):
    result = 0
    for i in range(a, b + 1):
        if isPrimeNum(i):
            result += i
    return result

print(sumPrimeNum(a, b))