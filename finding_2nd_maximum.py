def max2():
    list1=list(input("enter the numbers separated by space: ").split())
    a=max(list1)
    for i in range(len(list1)):
        if a in list1:
            list1.remove(a)
    print(max(list1))
