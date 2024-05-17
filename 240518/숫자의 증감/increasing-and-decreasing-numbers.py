c, n = map(str, input().split())
n = int(n)
print(' '.join(map(str, range(1, n + 1) if c == 'A' else range(n, 0, -1))))