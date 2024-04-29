def mini(arr,n):
    i=0
    j=n-1
    while j>=i+1:
        if arr[i]==arr[j]:
            arr[i]=1
            arr[j]=0
            break
        elif arr[i]==0 and arr[j]==1:
            arr[j]=0
            break
        elif arr[i]==1 and arr[j]==0:
            i+=1
            j-=1
    sum=0
    numZ=arr.count(0)
    for i in arr:
        if i==1:
            sum+=numZ
        else:
            numZ-=1
    return sum
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(mini(arr,n))