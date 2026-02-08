```
Correct Logic (think in states 🧥)

Initially: wearing = False

For each day:

If T < A
→ Chef must wear jacket
→ If not wearing already → count++

If T > B
→ Chef must remove jacket

If A ≤ T ≤ B
→ Chef can keep whatever he’s wearing (do nothing)
```

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
    
