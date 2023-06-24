n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
for i in arr:
    print("".join(map(str,i)))
d=[]
nd=[]
ud=[]
ld=[]
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            d.append(arr[i][j])
        if i!=j:
            nd.append(arr[i][j])
        if i<j:
            ud.append(arr[i][j])
        if i>j:
            ld.append(arr[i][j])
#task 1
print("Diagonal elements:",d)
print("Non-Diagonal elements:",nd)
print("Upper-Diagonal elements:",ud)
print("Lower-Diagonal elements:",ld)
#task 2
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print(arr[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("")

for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            print(arr[i][j],end=" ")
        else:
            print(" ",end=" ")
    print("")