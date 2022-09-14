def num(l):
    a=int(input("enter int number -> "))
    for i in l:
        if(i==a):
            print("Yes")
            return 0
    print("no")        


l=range(1,5)
num(l)