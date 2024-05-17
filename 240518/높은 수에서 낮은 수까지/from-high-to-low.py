a, b = map(int, input().split())
print(' '.join(map(str, range(a, b - 1, -1) if a > b else range(b, a - 1, -1))))