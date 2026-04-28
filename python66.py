# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"
# NOTE: All numbers will be whole numbers greater than 0.

# If you liked this kata, check out part 2!!

def expanded_form(num):
    m=str(num)
    l=len(m)
    new_str=""
    for i in m:
        i=int(i)
        if i!=0:
            i=i*(10**(l-1))
            new_str+=str(i)
            new_str+=" + "
        l-=1
    l=len(new_str)
    return new_str[:(l-3)]
    pass
