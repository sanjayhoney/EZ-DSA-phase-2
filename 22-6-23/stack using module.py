#stack using module
from queue import LifoQueue
s=LifoQueue(maxsize=3)
print(s.qsize())
s.put('b')
s.put('r')
s.put('t')
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())

#get combination of parenthesis as input and check whether it is balanced or not
b=[]
s=input()
if 

