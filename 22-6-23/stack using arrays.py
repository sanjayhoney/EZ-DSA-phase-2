#STACK
'''this follows lifo concept which is last in first out
stack implementation:
    1.using arrays
    2.using linked list
    3.using inbuild module
note: insertion and deletion happens at one end in stack which is on top.'''
 
stack=[]
def push():
    ele=int(input("enter the element:"))
    stack.append(ele)
def peek():
    if not stack:
        print("empty")
    else:
        print(stack[-1])
def pop():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element:",e)
def display():
    if not stack:
        print("empty")
    else:
        print(stack)
while True:
    print("select operation: 1.push 2.pop 3.display 4.peek 5.quit")
    choice=int(input("enter:"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        break
    else:
        print("enter correct operation!")
        
