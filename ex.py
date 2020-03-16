a=[]
n=10000
for i in range(0,n):
    a.append(int(input()))
k=30001
for i in range(0,n):
    if a[i]%4==0 and a[i]<k:
        k=a[i]
for i in range(0,n):
    if a[i]%4==0:
        a[i]=k
        print(a[i])
