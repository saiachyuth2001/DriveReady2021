num,k=map(int,input().split())
a=b=c=0
while num!=0:
    r=num%10
    num=num//10
    if(r==k):
        a=a+1
if(a>0):
    print("True")
else:
    print("False")
    
