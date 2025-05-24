a, b = map(int, input().split())

# Please write your code here.
def find_num(a, b):
    return sum(
        i % 3 == 0 or any(d in str(i) for d in '369')
        for i in range(a, b + 1)
    )

print(find_num(a, b))