### program3.py (character is present or not)

s = input()

found = False
for ch in s:
    if ch == 'A':
        found = True
        break

if found:
    print("YES")
else:
    print("NO")

### program4.py (palindrome number)

def check_palindrome(s):
    # Complete the function
    left=0
    right=len(s)-1
    issame=1
    while left<right:
        if s[left]!=s[right]:
            issame=0
            break
        left+=1
        right-=1
    return "YES" if issame==1 else "NO"

def main():
    test_cases = int(input())
    # Complete the function
    for i in range(test_cases):
        stre=input()
        print(check_palindrome(stre))
    
main()
