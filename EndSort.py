arr=[int(x) for x in input().split()]
arrsorted=sorted(arr)
c=0
for i in range(0,len(arr)):
    if arr[i]== arrsorted[c]:
        c+=1
print(len(arr)-c)
