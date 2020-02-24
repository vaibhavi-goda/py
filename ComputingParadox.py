n=int(input())
a=list(map(int,input().split()))
k=int(input())
key=a[k-1]
a.sort()
for i in range(len(a)):
    if key==a[i]:
        print(i+1)
        break
