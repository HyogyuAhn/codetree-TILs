genderNum = int(input())
age = int(input())
if genderNum == 0:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")
else:
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")