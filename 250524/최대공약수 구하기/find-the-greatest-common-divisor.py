n, m = map(int, input().split())

# Please write your code here.
def gcd(n, m):
    while m:
        n, m = m, n % m
    print(n)

gcd(n, m)