cold1, temp1 = input().split()
cold2, temp2 = input().split()
cold3, temp3 = input().split()
emer = 0
people = [[cold1, int(temp1)], [cold2, int(temp2)], [cold3, int(temp3)]]
for i in range(3):
    if people[i][0] == "Y" and people[i][1] >= 37:
        emer += 1
    if emer >= 2:
        print("E")
        break
if emer < 2:
    print("N")