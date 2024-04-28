am, ae = map(int, input().split())
bm, me = map(int, input().split())
if am > bm:
    print("A")
elif am < bm:
    print("B")
else:
    if ae > be:
        print("A")
    else:
        print("B")