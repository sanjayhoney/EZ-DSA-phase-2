#Write a function in python that checks if paranthesis in the string are balanced or not.
#Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def size(self):
        return len(self.container)
def match(ch1, ch2):
    match_dict={')': '(',']': '[','}': '{'}
    return match_dict[ch1] == ch2
def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not match(ch,stack.pop()):
                return False

    return stack.size()==0
s=input("Enter:")
x=is_balanced(s)
print(x)
