def odd_one(L):
    inti=0
    f=0
    s=0
    b=0
    for i in range (len(L)):
        if(type(L[i])==type(2)):
            inti=inti+1
        elif(type(L[i])==type(3.4)):
            f=f+1
        elif(type(L[i])==type('t')):
            s=s+1
        elif(type(L[i])==type(True)):
            b=b+1 
    if(inti==1): 
        return("int") 
    if(f==1): 
        return("float") 
    if(s==1): 
        return("str") 
    if(b==1): 
        return("bool") 
L=[2,3,4,5,6,7,2.4]
print(odd_one(L))          
    
    