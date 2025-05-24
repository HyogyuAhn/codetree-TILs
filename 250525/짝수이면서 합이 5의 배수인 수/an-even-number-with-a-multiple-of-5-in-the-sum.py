n = int(input())

# Please write your code here.
def sumIsFiveMulti(n):
    return sum(int(d) for d in str(n)) % 5 == 0 and n % 2 == 0

print("Yes" if sumIsFiveMulti(n) else "No")