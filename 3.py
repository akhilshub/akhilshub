b= '899999934'
k=0
d=0
while(k<=4):
    for i in range(k,k+5):
            if(b[k]==b[i]):
                d+=1
            if(d>=5):
                print('invalid')
                print(d)
                break 
    print(k , d)
    k+=1
    d=0
    
    