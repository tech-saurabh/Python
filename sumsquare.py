def sumofsquares(n):
    i=1
    while(i*i<=n):
        for i in range(1,n+1):
          a=i*i
        for j in range(1,n+1):
            b=j*j
            if((a+b)==n):
                 print("true")
    else:
        print("false")
