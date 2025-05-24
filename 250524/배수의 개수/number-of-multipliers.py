nums = [int(input()) for _ in range(10)]
m3 = sum(n % 3 == 0 for n in nums)
m5 = sum(n % 5 == 0 for n in nums)
print(f'{m3} {m5}')