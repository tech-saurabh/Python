n=int(input())
b=[]
for i in range(n):
    name=input()
    score=float(input())
    a=list([name,score])
    b.append(a)
list1=sorted(set(x[1] for x in b))
for name in sorted(x[0] for x in b if x[1]==list1[1]):
    print(name)
#c=max(b,key=lambda x:x[1])
#print(c)

