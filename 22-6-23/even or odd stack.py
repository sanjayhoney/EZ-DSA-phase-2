#create a stack using user input and extract only even numbers
stack=[]
def push():
    n=int(input("element: "))
    stack.append(n)
    print(stack)
def odd():
    odd=[i for i in stack if i%2!=0]
    print(odd)
def even():
    even=[i for i in stack if i%2==0]
    print(even)
while True:
    print("selectt ur choice: 0.push 1.even 2.odd 3.quit")
    choice=int(input("enter ur choice: "))
    if choice==0:
        push()
    elif choice==1:
        even()
    elif choice==2:
        odd()
    elif choice==3:
        break
    else:
        print("enter correct choice!")
    
