N = int(input())
A = []

for _ in range(N):
    line = input().split()
    cmd = line[0]
    if cmd == "push_front":
        A.insert(0, int(line[1]))
    elif cmd == "push_back":
        A.append(int(line[1]))
    elif cmd == "pop_front":
        print(A.pop(0))
    elif cmd == "pop_back":
        print(A.pop())
    elif cmd == "size":
        print(len(A))
    elif cmd == "empty":
        print("0") if A else print("1")
    elif cmd == "front":
        print(A[0])
    elif cmd == "back":
        print(A[len(A) - 1])