# There is an array with some numbers. All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

def find_uniq(arr):
    # your code here
    dicte={}
    for i in arr:
        if i in dicte:
            dicte[i]+=1
        else:
            dicte[i]=1
    for k,val in dicte.items():
        if val==1:
            return k
    return 1   # n: unique number in the array
