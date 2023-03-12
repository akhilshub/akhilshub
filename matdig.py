def matrix_type(M):
    k=len(M)
    di=0
    ds=0
    s=0
    a=M[0][0]
    for i in range(k):
        for j in range(k):
            if (i!=j):
                s=s+M[i][j]
            elif(i==j):
                if(M[i][j]==1):
                    di=di+1
                if(M[i][j]==a):
                    ds=ds+a
    if(s!=0):
        return("non-diagonal")
    elif(di==k):
        return("identity")
    elif(ds==(k*a)):
        return("scalar")
    else :
        return("diagonal")

                
    