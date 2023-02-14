#Stack class that implemets the most commen operations of a stack datastructure
#Without using the build in operation like pop or push, for a task in class
class Stack(object):
    def __init__(self):
        self.TOP = -1
        self.stack = []
    
    def push(self,value):
        self.stack.append(value)
        self.TOP += 1
        print("added:",value,"to stack")

    def cheackEmpty(self):
        if self.TOP == -1:
            print("stack is empty")
        else:
            print("stack not empty")
    
    def pop(self):
        if self.TOP == -1:
            print("Stack already empty")
            return
        print("removed", self.stack[self.TOP], "from Stack")
        self.stack.remove(self.stack[self.TOP])
        self.TOP -=1
    
    def peek(self):
        print (self.stack[self.TOP])