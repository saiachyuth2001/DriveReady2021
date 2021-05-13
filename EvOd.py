num=int(input())
a=b=c=0
k=num
while num!=0:
    r=num%10
    num=num//10
    c+=1
    if(r%2==0):
        a=a+1
        
    else:
        b=b+1
if(c==a):
    print("EVEN")
if(c==b):
    print("ODD")
if(k%2==0 and b!=0):
    print("Even Odd")
if(k%2!=0 and a!=0):
    print("Odd Even")
