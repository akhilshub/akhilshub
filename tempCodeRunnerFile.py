def sort(a):
    min=0
    for i in range (len(a)):
        if(a[i]>min):
            temp=min
            min=a[i]
            a[i]=temp
    return(a)

a=[3,5,2,3,542,45,2]
print(sort(a))