
n=[]
n=input().split(',')
d=[]
d=input().split(',')
common=[]
for i in range(len(d)):
    #l=append.n[i]
    l=[]
    for j in range(i,len(d)):
        if(d[i]==d[j]):
           l.append(n[j])
    m=[]    
    for k in range(len(l)-1):
        m.append(l[k])
        m.append(l[k+1])
        common.append(m)
        m=[]
               
print(common)    
        