# Remove n exclamation marks in the sentence from left to right. n is positive integer.

# Examples
# remove("Hi!",1) === "Hi"
# remove("Hi!",100) === "Hi"
# remove("Hi!!!",1) === "Hi!!"
# remove("Hi!!!",100) === "Hi"
# remove("!Hi",1) === "Hi"
# remove("!Hi!",1) === "Hi!"
# remove("!Hi!",100) === "Hi"
# remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
# remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"

def remove(st, n):
    if n==0:
        return st
    new_str=""
    count=0
    for i in st:
        if i=='!':
            if count!=n:
                count+=1
            else:
                new_str+=i
        else:
            new_str+=i
    return new_str
    pass
