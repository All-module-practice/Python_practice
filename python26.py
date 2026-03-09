# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    counto=0
    countx=0    
    for i in s:
        if i.lower()=='o':
            counto+=1
        if i.lower()=='x':
            countx+=1
    if counto==countx:
        return 1
    return 0
    pass
