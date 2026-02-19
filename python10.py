# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

def ips_between(start, end):
    # TODO
    a,b,c,d=map(int,start.split('.'))
    a1,b1,c1,d1=map(int,end.split('.'))
    sum1=a*(256**3)+b*(256**2)+c*256+d
    sum2=a1*(256**3)+b1*(256**2)+c1*256+d1
    return sum2-sum1
