M, D = map(int, input().split())

# Please write your code here.
dayMax = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isExistDate(M, D):
    return "Yes" if 1 <= M <= 12 and D <= dayMax[M] else "No"

print(isExistDate(M, D))