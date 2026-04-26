# Given a string str, reverse it and omit all non-alphabetic characters.

# Example
# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".

# Input/Output
# [input] string str
# A string consists of lowercase latin letters, digits and symbols.

# [output] a string

def reverse_letter(st):
    new_str=""
    n=len(st)
    while n>0:
        if st[n-1]>='a' and st[n-1]<='z':
            new_str+=st[n-1]
        n-=1
    return new_str
