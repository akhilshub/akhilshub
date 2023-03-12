n=input()
sl=0

n1=""
sr=0
k1=len(n)
for i in range(k1):
    if(n[i]!=','):
        n1=n1+n[i]
k=len(n1)
for i in range(int(k/2)):
    sl=sl+int(n1[i])
for i in range(int(k/2),k):
    sr=sr+int(n1[i])
print (sl)
print(sr)    
if(sl>sr):
    print("left-heavy")  
elif(sl<sr):
    print("right-heavy")     
else :
    print('balanced')