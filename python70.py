# Complete the function which converts a binary number (given as a string) to a decimal number.

def bin_to_decimal(inp):
    l=len(inp)-1
    decimal=0
    for i in inp:
        if i=='1':
            decimal+=(2**l)
        l-=1
    return decimal
    pass
