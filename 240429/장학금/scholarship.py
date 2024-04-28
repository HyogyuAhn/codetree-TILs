ms, fs = map(int, input().split())
if ms >= 90:
    if fs >= 95:
        print("100000")
    elif fs < 95 and fs >= 90:
        print("50000")
    else:
        print("0")
else:
    print("0")