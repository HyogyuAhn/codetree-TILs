a, b = map(int, input().split())
result = a / b
result_str = str(result)
decimal_point_index = result_str.find('.')
if decimal_point_index == -1:
    result_str += '.00000000000000000000'
else:
    decimal_length = len(result_str) - decimal_point_index - 1
    while decimal_length < 20:
        result_str += '0'
        decimal_length += 1
    if decimal_length > 20:
        result_str = result_str[:decimal_point_index + 1 + 20]
integer_part, decimal_part = result_str.split('.')
final_result = integer_part + '.' + decimal_part[:21]
print(f"{final_result}")