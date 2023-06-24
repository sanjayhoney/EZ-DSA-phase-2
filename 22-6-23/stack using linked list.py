#stack implementation using linked list
'''inserting node at last and deleting the last node becomes stack'''


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.self.head
            self.head=newnode
    def pop(self):
        if self.head is None:
            return None
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped
objs=stack()
while True:
    print('Push <value>')
    print('Pop')
    print('Quit')
    do = input('What would you like to do ?').split()
    print('do',do)
    print('do[0]',do[0])
    operation=do[0].strip().lower()
    if operation == 'push':
        objs.push(int(do[1]))
    elif operation == 'pop':
        popped =objs.pop()
        if popped is None:
            print('Stack is Empty!')
        else:
            print('Popped value: ',int(popped))
            
'''method 2
while implementing stack using linked list we can opt this method also.
Here we do insert node at beginning deleting the head node or first node.
note:
    In these above 2 methods second one is efficient because in the 1st method
    to do the pop operation we have to traverse till last node'''    
