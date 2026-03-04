# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

def accum(st):
    n=len(st)
    li=[]
    for i in range(n):
        ch=st[i]
        li.append(ch.upper())
        if i!=0:
            for j in range(i):
                li.append(ch.lower())
        if i!=(n-1):
            li.append('-')
    return "".join(li)
