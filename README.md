### program1.py

```
print("-_-"*10+"| Hi,This is souvik |"+"-_-"*10)
```

### program2.py (Codeforce style(with testcase))

```
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)
```

### program3.py (character is present or not)

```
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
```

### program4.py (palindrome number)

```
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

```
⏱ Time & Space Complexity (exam-ready)

Time: O(n) per string

Space: O(1) (no extra data structures)

“I used the two-pointer technique, comparing characters from both ends and moving toward the center.”

```

### program5.py

```
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        li=[]

        for i in range(n):
            li.append(nums[i])
            li.append(nums[n+i])
        return li
```

### program6.py

```
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
```

### program7.py

```
def solution(text, ending):
    # your code here...
    
    list1=list(text)
    list2=list(ending)
    
    
    list3=list1[-len(list2):]
    
    
    print(list3==list2)

t1="samurai"
e1="ai"

solution(t1,e1)
```

#### Another approaches

🧠 Even Simpler (No lists needed)

Strings already support slicing:

```
def solution(text, ending):
    return text[-len(ending):] == ending
```

```
🔥 Cleanest Way (Best Practice)
def solution(text, ending):
    return text.endswith(ending)
```

### program8.py

```
📝 Notes – Ordering Words by Number in String
🎯 Problem

Given a sentence:

"is2 Thi1s T4est 3a"


Each word contains a number.
We must arrange the words according to that number.

Output:

"Thi1s is2 3a T4est"

🔎 Code Explanation Step-by-Step
def order(sentence):


👉 Define a function named order that takes one input: sentence.

    if not sentence:
        return ""


👉 If the sentence is empty (""), return empty string.
This prevents errors.

    words = sentence.split()


👉 .split() converts string into list of words.

Example:

"is2 Thi1s T4est 3a".split()


Becomes:

['is2', 'Thi1s', 'T4est', '3a']

    l = len(words)


👉 Count number of words.

    list2 = [None] * l


👉 Create an empty list with same size as words.

Example:

[None, None, None, None]


We will place words in correct positions here.

    for word in words:


👉 Loop through each word.

        for ch in word:


👉 Loop through each character in the word.

Example:

"Thi1s" → T, h, i, 1, s

            if ch.isdigit():


👉 Check if character is a number.

                num = int(ch)


👉 Convert the digit from string to integer.

Example:

"1" → 1

                list2[num - 1] = word


👉 Place the word in correct position.

Why num - 1?

Because:

List index starts from 0

But numbers start from 1

Example:
If number is 1, position should be index 0.

                break


👉 Stop checking once number is found.

    stre = " ".join(list2)


👉 Join list back into a string with spaces.

Example:

['Thi1s', 'is2', '3a', 'T4est']


Becomes:

"Thi1s is2 3a T4est"

    return stre


👉 Return the final ordered sentence.

🧠 Important Concepts Used

✔ Functions
✔ if condition
✔ for loops
✔ Nested loops
✔ String iteration
✔ .isdigit()
✔ List indexing
✔ .split()
✔ " ".join()
✔ break statement
```

code:

```
def order(sentence):
    if not sentence:
        return ""
    words=sentence.split()
    l=len(words)
    list2=[None]*l
    for word in words:
        for ch in word:
            if ch.isdigit():
                num=int(ch)
                list2[num-1]=word
                break
    stre=" ".join(list2)
    return stre
    pass


sen="is2 Thi1s T4est 3a"
num=order(sen)

print(num)
```
