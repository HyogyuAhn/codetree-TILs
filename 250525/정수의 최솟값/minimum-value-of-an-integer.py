a, b, c = map(int, input().split())

# Please write your code here.
def find_min(a, b, c):
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)

print(find_min(a, b, c))