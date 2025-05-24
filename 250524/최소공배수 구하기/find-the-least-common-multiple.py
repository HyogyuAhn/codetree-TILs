n, m = map(int, input().split())

# Please write your code here.
def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

def lcm(n, m):
    return n * m // gcd(n, m)

print(lcm(n, m))