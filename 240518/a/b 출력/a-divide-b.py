a, b = map(int, input().split())
x = a % b
result = f"{a//b}."
for _ in range(20):
    x *= 10
    result += f"{x//b}"
    x %= b

print(result)