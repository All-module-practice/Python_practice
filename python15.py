# A drink is called fanta-like if the last three letters of its name are 'n', 't', and 'a', in that order.
# In other words, the name of the drink must end with "nta".

# You bought a drink from a vending machine.
# The name of the drink is represented by the string S.

# It is guaranteed that S consists of exactly 5 lowercase English letters.

# Determine whether the drink is fanta-like.

a=input()
if a[len(a)-3:]=='nta':
    print("Yes")
else:
    print("No")
