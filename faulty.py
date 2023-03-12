n=input("a no.")
i=0
c=0
s=""
if("l" in n or "o" in n):
    for i in range(10):
        a=n[i]
        if(a == 'l'):
            c=c+1
            s=s+'1'
        elif(a=='o'):
            c=c+1
            s=s+'0'
        else:
            s=s+a        
    
    print(str(c)+" mistakes")
    print (s)
else:
    print("No mistakes")    