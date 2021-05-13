T= int(input())
a=b=c=d=e=0

for _ in range(T):
    S=input()
    for i in range(len(S)):
        if(((S[i]=="A")and(S[i]=="a"))or((S[i]=="A")or(S[i]=="a"))):
            a+=1
        if(((S[i]=="E")and(S[i]=="e"))or((S[i]=="E")or(S[i]=="e"))):
            b+=1
        if(((S[i]=="I")and(S[i]=="i"))or((S[i]=="I")or(S[i]=="i"))):
            c+=1
        if(((S[i]=="O")and(S[i]=="o"))or((S[i]=="O")or(S[i]=="o"))):
            d+=1
        if(((S[i]=="U")and(S[i]=="u"))or((S[i]=="U")or(S[i]=="u"))):
            e+=1
        if((S[i]=="A")or(S[i]=="E")or(S[i]=="I")or(S[i]=="O")or(S[i]=="U")):
            f+=1
        if((S[i]=="a")or(S[i]=="e")or(S[i]=="i")or(S[i]=="o")or(S[i]=="u")):
            g+=1
        
                   
    if((a>0)and(b>0)and(c>0)and(d>0)and(e>0)and(f>4)and(f>4)):
        print("lovely string")
    else:
        print("ugly string")

