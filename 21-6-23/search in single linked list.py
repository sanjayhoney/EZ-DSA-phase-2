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
            
    def search(self,b):
        temp=self.head
        while(temp):
            if temp.data==b:
                print("yes")
                break
            temp=temp.next
        else:
            print("not present")
        
    def insert_beg(self, data):
        newnode= Node(data)
        newnode.next=self.head
        self.head=newnode
        
        
    def insert_end(self,data):
        newnode = Node(data)
        curr=self.head
        if self.head is None:
            print("list is empty")
        else:
            while curr.next:
                curr=curr.next
            curr.next=newnode
    
            
    def insert_pos(self,data,position):
        if position<=0:
            self.insert_at_beg(data)
        else:
            newnode=Node(data)
            curr=self.head
            for i in range(position-1):
                curr=curr.next
            newnode.next=curr.next
            curr.next=newnode
            
    def delete_beg(self):
        if self.head is None:
            print("list is empty")
        else:
            self.head=self.head.next
    def delete_end(self):
        curr=self.head.next
        prev=self.head
        while curr.next is not None:
            curr=curr.next
            prev=prev.next
        prev.next=None
    def delete_pos(self,pos):
        curr=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            curr=curr.next
            prev=prev.next
        prev.next=curr.next
        curr.next=None
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
n4.next=n5
obj.display()
obj.insert_beg(2)
obj.display()
obj.insert_pos(10,2)
obj.display()
obj.insert_end(5)
obj.display()
obj.delete_beg()
obj.display()
obj.insert_pos(9,4)
obj.display()
obj.delete_end()
obj.display()
obj.delete_pos(3)
obj.display()
b=int(input("enter no. to search:"))
obj.search(b)
