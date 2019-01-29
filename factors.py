def factor(n):
    factors=[]
    for i in range(1,n+1):
        if(n%i)==0:
            factors.append(i)
    print(factors)

            
    
def isprime(n):
    two=[1,n]
    return(factor(n)==two)

    

