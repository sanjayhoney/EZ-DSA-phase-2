#linked list containing loop or cycle
''''floyds algorithm is used to find out whether a linked contains cycle or not
floyds algorithm:
    1.to find out the meeting point if there is cycle assign two
    pointers to head node.
    2. one pointer will jump 1 step another will jump 2 steps at a time.
    3. if they are meeting at 1 node, we declare linked list contains
    loop or cycle & that node is called as meeting point.
finding start node of cycle:
    1. assign 2 pointers, 1 with head node and another with meeting point node.
    2. now, both of them will jump 1 step at a time.
    3. where they are meeting is called starting node of the cycle.
removing cycle from linked list:
    1. find out the node which is connected with starting node of the cycle,
    and make its next as none.
m.p= meeting point
s.p= start point

                                    m.p/s.p
|=|=|--> |=|=|--> |=|=|--> |=|=|--> |=|=|--> |=|=|
                                   |             |
                                   |             |
                                   |=|=| <--|=|=|<                 '''


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def push(self,ndata):
        nnode=Node(ndata)
        nnode.next=self.head
        self.head=nnode
    def detectandremoveloop(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        slowp=self.head
        fastp=self.head
        while(slowp and fastp and fastp.next):
            slowp=slowp.next
            fastp=fastp.next.next
            if slowp==fastp:
                print("meeting point:",slowp.data)
                slowp=self.head
                while(slowp.next!=fastp.next):
                    slowp=slowp.next
                    fastp=fastp.next
                print("start of loop",fastp.next.data)
                fastp.next=None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=' ')
            temp=temp.next
lst=Linkedlist()
lst.head=Node(50)
lst.head.next=Node(20)
lst.head.next.next=Node(15)
lst.head.next.next.next=Node(4)
lst.head.next.next.next.next=Node(10)
extra=Node(1)
lst.head.next.next.next.next.next=extra
extra.next=lst.head.next
lst.detectandremoveloop()
print("linked list after removing loop")
lst.printlist()
