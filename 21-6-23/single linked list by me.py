class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:   
            print("list is empty")
        else:
            currentnode=self.head
            while currentnode.next:
                print(currentnode.data, end="->")
                currentnode=currentnode.next
            print(currentnode.data)
            
            
    def insert_at_beg(self, data):
        newnode= Node(data)
        newnode.next=self.head
        self.head=newnode
        
        
    def insert_at_last(self,data):
        newnode = Node(data)
        curr=self.head
        if self.head is None:
            print("list is empty")
        else:
            while curr.next:
                curr=curr.next
            curr.next=newnode
    
            
    def insert_at_position(self,data,position):
        if position<=0:
            self.insert_at_beg(data)
        else:
            newnode=Node(data)
            curr=self.head
            for i in range(position-1):
                curr=curr.next
            newnode.next=curr.next
            curr.next=newnode
            
    def delete_at_beg(self):
        if self.head is None:
            print("list is empty")
        else:
            self.head=self.head.next
    def delete_at_end(self):
        curr=self.head
        if curr is None:
            print("list is empty")
        elif curr.next is None:
            curr=None
        else:
            current=self.head
            while current.next.next:
                current=current.next
            current.next=None
    

                
  
        
    

obj=SLL()
n=Node(1)
obj.head=n
n1=Node(2)
obj.head.next=n1
n2=Node(3)
n1.next=n2
n3=Node(4)
n2.next=n3
n4=Node(5)
n3.next=n4
n5=Node(6)
n4.next
obj.display()
obj.insert_at_beg(8)
obj.display()
obj.insert_at_beg(9)
obj.display()
obj.insert_at_last(10)
obj.display()
obj.delete_at_beg()
obj.display()
obj.insert_at_position(134,3)
obj.display()
obj.insert_at_position(568,9)
obj.display()
obj.delete_at_end()
obj.display()
'''circular linked list:
the last node will be connected with 1st node now it becomes a circular linked list output
will be infinite loop'''




