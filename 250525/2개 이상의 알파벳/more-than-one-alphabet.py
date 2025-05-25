A = input()

# Please write your code here.
def checkAlphaCnt(s):
    alpha = None
    for d in s:
        if alpha != None and alpha != d:
            return "Yes"
        elif alpha == None:
            alpha = d
        else:
            return "No"

print(checkAlphaCnt(A))