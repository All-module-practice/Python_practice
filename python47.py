# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    mult=1
    for i in arr:
        mult*=i
    return mult
    pass
