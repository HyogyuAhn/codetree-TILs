import random
from decimal import Decimal, getcontext, ROUND_DOWN

a, b = map(int, input().split())
getcontext().prec = 20
result = Decimal(a) / Decimal(b)
rounded_result = result.quantize(Decimal('0.00000000000000000000'), rounding=ROUND_DOWN)
print(f"{rounded_result}")