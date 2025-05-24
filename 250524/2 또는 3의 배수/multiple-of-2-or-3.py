a = int(input())
for i in range(1, a + 1):
    print(1, end = ' ') if i % 2 == 0 or i % 3 == 0 else print(0, end = ' ')