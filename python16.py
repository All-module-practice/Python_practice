# The Tribonacci sequence is a generalization of the Fibonacci sequence.

# In the Fibonacci sequence, each term is the sum of the previous two terms.

# In the Tribonacci sequence, each term is the sum of the previous three terms: 

# 📌 Task

# Create a function tribonacci(signature, n) that:

# Takes a signature list containing exactly 3 numbers

# Returns the first n elements of the Tribonacci sequence

# The signature values must be included in the result

# If n == 0, return an empty list []

# Method 1

def tribonacci(signature, n):
    li=[]
    if n==0:
        return li
    a=signature[0]
    b=signature[1]
    c=signature[2]
    if  n==1:
        li.append(a)
        return li
    if n==2:
        li.append(a)
        li.append(b)
        return li
    li.append(a)
    li.append(b)
    li.append(c)
    if n==3:
        return li
    for i in range(3,n):
        num=li[i-3]+li[i-2]+li[i-1]
        li.append(num)
    return li
    pass

# Method 2

def tribonacci(signature, n):
    li=[]
    if n==0:
        return li
    li=signature[:n]
    for i in range(3,n):
        num=li[i-3]+li[i-2]+li[i-1]
        li.append(num)
    return li
    pass
