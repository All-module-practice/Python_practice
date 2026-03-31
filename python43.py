# The Fibonacci numbers are the numbers in the following integer sequence (Fn): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

# such that:
# F(0) = 0
# F(1) = 1
# F(n) = F(n - 1) + F(n - 2)
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n + 1) verifying:
# F(n) * F(n + 1) = prod

def product_fib(_prod):
    first_num=0
    sec_num=1
    while True:
        if (first_num*sec_num)==_prod:
            return [first_num,sec_num,True]
        elif (first_num*sec_num)>_prod:
            return [first_num,sec_num,False]
        sum=first_num+sec_num
        first_num=sec_num
        sec_num=sum
    pass
