# cook your dish here
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    wearing=False
    count=0
    for j in range(n):
        num=arr[j]
        if num<a:
            if not wearing:
                count+=1
                wearing=True
        elif num>b:
            wearing=False
    print(count)
    
