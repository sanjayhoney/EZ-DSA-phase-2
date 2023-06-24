n=int(input())
lst=list(map(int,input().split()))
print(lst)

print("""1.append
2.pop
3.sort
4.insert
5.pop with element
6.search""")
y=input().lower()
while y is 'y':
    x=int(input())
    if x==1:
        j=int(input())
        if j in lst:
            print("the num is already presnt in the lst")
            print("however if you want to insert press (y): ")
            yes=input().lower()
            if yes=="y":
                lst.append(j)
            else:
                print("the previous list is: ",lst)
            lst.append(j)
            print(lst)
            y=input("do u want to perform opns again ?: ")
    elif x==2:
        lst.pop()
        print(lst)
        y=input("do u want to perform opns again ?: ")
    elif x==3:
        lst.sort()
        print(lst)
        y=input("do u want to perform opns again ?: ")
    elif x==4:
        p=int(input("positon: "))
        num=int(input("number:"))
        lst.insert(p, num)
        print(lst)
        y=input("do u want to perform opns again ?: ")
    elif x==5:
        i=int(input("num u wnt to del:"))
        lst.pop(i)
        print(lst)
        y=input("do u want to perform opns again ?: ")
    elif x==6:
        y=int(input("search: "))
        if y in lst:
            print(y, "is there")
        else:
            pass
            print(y, "is not in lst")
