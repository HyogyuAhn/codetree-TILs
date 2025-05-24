n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# -1 시작 0 같은 수 발견 1 연속체크 완료
# Please write your code here.
def isConSeq(seq1, seq2):
    size1, size2 = len(seq1), len(seq2)
    for i in range(size1 - size2 + 1):
        if seq1[i:i+size2] == seq2:
            return True
    return False


print('Yes' if isConSeq(a, b) else 'No')