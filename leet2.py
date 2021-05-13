a=list(map(int,input().split()))
s=[]
c=0
k=len(a)
r=int(input("R: "))
for i in range(k):
    for j in range(k):
        if i<j:
            c=a[i]+a[j]
        if c==r:
            s.append(i)
            s.append(j)
            
        
print(s)
            
            
        
