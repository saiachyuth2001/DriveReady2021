#### n(=5) Table upto 20 ##
#### input 5 3 10 or 5 10 3 it must give the table
####num,a,val=map(int,input().split())
####if a>val:
####    a,val=val,a
####for i in range(a,val+1):
####    print(num,"x",i, '=',i*num)


##num,a,val=map(int,input().split())#5 10 3 
##d1=1
##if a>val:
##    #a,val=val,a
##    d1=-1
##for i in range(a,val+d1,d1):
##    print(num,"x",i, '=',i*num)


##num,val=map(int,input().split())#5 20
##for i in range(1,val+1):
##    if i%num==0:#20%5==0
##        continue
##    print(num,"x",i, '=',i*num)


### if we give input 5 20 then it should print upto 5 x 4 = 20
##num,val=map(int,input().split())#5 20
##for i in range(1,val+1):#1
##    s=i*num#20
##    print(num,"x",i, '=',s)
##    if s==val:#20==20
##        break
##    
