Y, M, D = map(int, input().split())

# Please write your code here.
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(Y):
    return Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0)

def printSeason(Y, M, D):
    if M < 1 or M > 12:
        print(-1)
        return
    max_day = 29 if M == 2 and isLeapYear(Y) else days[M]
    if D < 1 or D > max_day:
        print(-1)
    elif 3 <= M <= 5:
        print("Spring")
    elif 6 <= M <= 8:
        print("Summer")
    elif 9 <= M <= 11:
        print("Fall")
    else:
        print("Winter")

printSeason(Y, M, D)