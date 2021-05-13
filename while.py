##n,m =map(int,input().split(","))
##i=n
##while i<=m:
##    print(i)
##    i+=1

# bwk loop #
n,m =map(int,input().split(","))
i=m
while i>=n:
    
    #i-=1
    if(i%3==0):
        #print(i)
        i-=1
        continue
        #print(i)
    print(i)   
    i-=1
    
