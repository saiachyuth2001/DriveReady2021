##num=int(input())
##a=b=s1=s2=s3=s4=0
##
##while num!=0:
##    r=num%10
##    num=num//10
##    if(r%2==0):
##        a=a+1
##        s1=s1*10+r
##    else:
##        b=b+1
##        s2=s2*10+r
###print(s1,s2)
##while s1:
##    r=s1%10
##    s1=s1//10
##    s3=s3*10+r
##while s2:
##    r=s2%10
##    s2=s2//10
##    s4=s4*10+r
##print(s3,s4)



##if(a%2==0):
##    print("even",end=" ")
##if(b%2!=0):
##    print("odd")
##if(a%2!=0 and b%2==0):
##    print("not even  not odd")




##
num=int(input())
a=b=c=s1=s2=s3=s4=0
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
