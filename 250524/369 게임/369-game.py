n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0 or any(j in str(i) for j in '369'):
        print('0', end = ' ')
    else:
        print(i, end = ' ')