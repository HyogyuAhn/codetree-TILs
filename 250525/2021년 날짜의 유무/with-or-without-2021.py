M, D = map(int, input().split())

# Please write your code here.
dayMax = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def isExistDate(M, D):
    return "Yes" if D <= dayMax[M] and 1 <= M <= 12 else "No"

print(isExistDate(M, D))