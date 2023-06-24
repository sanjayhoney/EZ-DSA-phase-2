deleting a node from linked list:
there are 3 types:
    1. deleting the 1st node
    2. deleting the last node
    3. deleting the node in between
1.deleting the 1st node:
    1.make the 2nd node as head node
    2.make the 1st node's head as null or none.
2.deleting the last node:
    1.traverse till last but before node.
    2.make its next as null.

begin:    
def delete(self):
    temp=self.head
    self.head=temp.next
    temp.next=None
end:
def delete(self):
    temp=self.head.next
    prev=self.head
    while temp.next is not None:
        temp=temp.next
        prev=prev.next
    prev.next=None#last but before node's next

inbetween position:
def del_position(self,pos):
    temp=self.head.next
    prev=self.hard
    #2 iterations
    for i in range(1,pos-1):
        temp=temp.next
        prev=prev.next
    prev.next=temp.next
    temp.next=None
            
