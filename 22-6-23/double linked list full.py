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
    def insert_at_end(self, data):
        newnode=Node(data)
        if self.head is None:
            self.head = newnode
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=newnode
            newnode.prev=curr
    def insert_at_pos(self,data,pos):
        if pos<=0:
            self.insert_at_beg(data)
        else:
            newnode=Node(data)
            curr=self.head
            for i in range(pos-1):
                curr=curr.next
            newnode.prev=curr
            newnode.next=curr.next
            curr.next.prev=newnode
            curr.next=newnode
    def delete_at_beg(self):
        curr=self.head
        if self.head is None:
            print("empty")
        else:
            self.head=self.head.next
            self.head.prev=None
    def delete_at_end(self):
        curr=self.head
        if self.head is None:
            print("empty")
        else:
            while curr.next.next:
                curr=curr.next
            curr.next.prev=None
            curr.next=None
    def delete_at_pos(self,pos):
        curr=self.head
        for i in range(pos-1):
            curr=curr.next
        if(curr.next.next!=None):
            curr.next.next.prev=curr
            curr.next=curr.next.next
        else:
            print("no")
    def search(self,n):
        curr=self.head
        if self.head is None:
            print("list is empty")
        else:
            while curr:
                if curr.data==n:
                    print("it is present")
                    break
                curr=curr.next
            else:
                print("not present")
            
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
lst.insert_at_pos(90,2)
lst.display()
lst.delete_at_beg()
lst.display()
lst.delete_at_end()
lst.display()
lst.delete_at_pos(3)
lst.display()
lst.delete_at_pos(1)
lst.display()
n=int(input())
lst.search(n)
