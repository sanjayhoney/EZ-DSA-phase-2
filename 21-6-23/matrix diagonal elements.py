n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
for i in arr:
    print("".join(map(str,i)))
for i in range(n):
    for j in range(n):
        if i==j:
            print(arr[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if i!=j:
            print(arr[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if (i==0 and j==1 or i==0 and j==2 or i==1 and j==2):
            print(arr[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n):
    for j in range(n):
        if (i==1 and j==0 or i==2 and j==0 or i==2 and j==1):
            print(arr[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()