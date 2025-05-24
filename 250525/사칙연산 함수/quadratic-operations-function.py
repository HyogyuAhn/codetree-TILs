a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def calc(a, o, b):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        return a // b
    else:
        return None

if calc(a, o, c) is not None:
    print(f'{a} {o} {c} = {calc(a, o, c)}')
else:
    print('False')