a, b = map(int, input().split())

# Please write your code here.
def calc(a, b):
    return (a + 25, b * 2) if a > b else (a * 2, b + 25)

a, b = calc(a, b)
print(a, b)