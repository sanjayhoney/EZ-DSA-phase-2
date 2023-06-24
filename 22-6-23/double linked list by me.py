class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head is None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            curr=self.head
            while curr.next:
                print(curr.data,end="<-->")
                curr=curr.next
            print(curr.data)
    def insert_at_beg(self,data):
        newnode=Node(data)
        if self.is_empty():
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def insert_at_end(self,data):
        newnode=Node(data)
        newnode.next=None
        curr=self.head
        if self.is_empty():
            print("empty")
        else:
            while curr.next:
                curr=curr.next
            curr.next=newnode
            newnode.prev=curr
lst=DLL()
n1=Node(100)
lst.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
n4=Node(400)
n4.prev=n3
n3.next=n4
lst.display()
lst.insert_at_beg(50)
lst.display()
lst.insert_at_end(90)
lst.display()