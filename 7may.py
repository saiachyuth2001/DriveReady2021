##T=int(input())
##for _ in range(T):
##    n=int(input())
##    if n%2==0:
##        print("even")
##    else:
##        print("odd")
##    


n=int(input())
s=0
k=n//7
p=k
#print(k)


while(k>=0):
    
    for i in range(k,n+1):
        
        s=s+i
        
    k-=1

print(s)

