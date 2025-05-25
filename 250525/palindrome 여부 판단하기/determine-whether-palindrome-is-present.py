A = input()

# Please write your code here.
def isPalindrome(text):
    return text == text[::-1]

if isPalindrome(A):
    print("Yes")
else:
    print("No")