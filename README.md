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
