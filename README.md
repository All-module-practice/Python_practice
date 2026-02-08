### program1.py

print("-_-"*10+"| Hi,This is souvik |"+"-_-"*10)

### program2.py (Codeforce style(with testcase))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)

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

```
⏱ Time & Space Complexity (exam-ready)

Time: O(n) per string

Space: O(1) (no extra data structures)

“I used the two-pointer technique, comparing characters from both ends and moving toward the center.”

```

### program5.py

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        li=[]

        for i in range(n):
            li.append(nums[i])
            li.append(nums[n+i])
        return li

### program6.py

# cook your dish here
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    wearing=False
    count=0
    for j in range(n):
        num=arr[j]
        if num<a:
            if not wearing:
                count+=1
                wearing=True
        elif num>b:
            wearing=False
    print(count)
    
