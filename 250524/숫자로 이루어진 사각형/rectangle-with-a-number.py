n = int(input())

# Please write your code here.
def print_square(n):
    for i in range(n):
        for j in range(n):
            print((i * n + j) % 9 + 1, end=' ')
        print()

print_square(n)