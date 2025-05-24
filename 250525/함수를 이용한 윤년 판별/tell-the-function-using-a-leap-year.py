y = int(input())

# Please write your code here.
def isLeapYear(y):
    return y % 4 == 0 and not (y % 100 == 0 and y % 400 != 0)

print('true' if isLeapYear(y) else "false")