a0,a1,a2,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,0,0,0,0,0,0
flag= True
b=input()
if(len(b)!=10):
     print ('invalid for length')
     flag= False
if(flag ):
     if( b[0]!='6'and b[0]!='7'and b[0]!='8' and b[0]!='9'):
       print('invalid start')
       flag= False
if(flag):   
    for c in b:
        if (c=='1'):
           a1+=1
        elif (c=='2'):
           a2+=1   
        elif (c=='3'):
           a3+=1
        elif (c=='4'):
           a4+=1
        elif (c=='5'):
           a5+=1
        elif (c=='6'):
           a6+=1
        elif (c=='7'):
           a7+=1  
        elif (c=='8'):
           a8+=1
        elif (c=='9'):
           a9+=1
        elif (c=='0'):
           a0+=1
        if( a0>7 or a1>=7 or a2>7 or a3>7 or a4>7 or a5>7 or a6>7 or a7>7 or a8>7 or a9>7):
            print('invalid seven same digits')
            flag= False
if(flag):
    d=1
    for i in range (len(b)-1):
        if(b[i]==b[i+1]):
            d+=1
           
        else:  
            if(d>5):
                print('invalid 5 continuous')
                flag= False
                break 
            d=1
if(flag):
    print('valid')        


    
    X=[1,3,2]
    dp = 0
for elem in X:
    dp += elem * elem
print(dp)    