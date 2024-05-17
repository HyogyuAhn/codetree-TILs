a, b = map(int, input().split())
quotient = a // b
remainder = a % b
result_str = str(quotient) + '.'

decimal_places = 0
while decimal_places < 20:
    remainder *= 10
    digit = remainder // b
    remainder = remainder % b
    result_str += str(digit)
    decimal_places += 1
print(f"{result_str}")