m3 = m5 = 0
for _ in range(10):
    i = int(input())
    if i % 3 == 0:
        m3 += 1
    if i % 5 == 0:
        m5 += 1
print(f'{m3} {m5}')