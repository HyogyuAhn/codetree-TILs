n = int(input())
for _ in range(n):
    i = int(input())
    if i % 3 == 0 and i % 2 != 0:
        print(i)