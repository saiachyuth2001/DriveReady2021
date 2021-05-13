n=int(input())
r=0
k=abs(n)
while(k>0):
    s=k%10
    r=r*10+s
    k=k//10
if(n<0):
    print("-",end="")
    print(r)
else:
    print(r)

