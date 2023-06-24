single linked list insertion
1. insert at beginning
2. insert at last
3. insert in between
 . insert at beginning:
  1.create the new node
  2. newnode.next=current head node
  3. head=newnode


new  next 
data   
   ^  ^
   |=|=|  |=|=|  |=|=|  |=|=|  |=|=|


def insert_beginning(self,data):
    nb=Node(data)
    nb.next=self.head
    self.head=nb
def display(self):
    if self.head is None:
        print("Linked list is empty")
    else:
        temp=self.head
        while temp:
            print(temp.data,"-->",end='')
            temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3.Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("before inserting 100")
obj.display()
print("")
print("after inserting 100")
obj.insert_beginning(100)
obj.display()
print("")
print("after inserting 555")
obj.insert_beginning(555)
