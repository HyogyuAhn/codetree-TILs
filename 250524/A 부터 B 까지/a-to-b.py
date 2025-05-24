a, b = map(int, input().split())
for _ in range(b):
    if a > b:
        break
    print(a, end = ' ')
    if a % 2 == 0:
        a += 3
    else:
        a *= 2