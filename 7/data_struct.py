
class LinkedList:
    class Node:
        def __init__(self, value = None, nxt = None):
            self.nxt = nxt
            self.val = value 
    class Iterator:
        def __init__(self, my_list):
            self.curr = my_list.head 
        def __next__(self):
            if self.curr:
                res = self.curr
                self.curr = self.curr.nxt
                return res
            raise StopIteration
        def __iter__(self):
            return self

    def __init__(self):
        self.head = None
        self.tail = None
    def add(self, val):
        self.head = self.Node(value = val, nxt = self.head)
        
        if not self.tail:
            self.tail = self.head
    def add_to_tail(self, val):
        node = self.Node(val)
        if not self.tail:
            self.tail = self.head = node
        else:
            self.tail.nxt = node
            self.tail = self.tail.nxt
            print(self.tail.val)
    def rm_head(self):
        if self.head: 
            self.head = self.head.nxt
    def print(self):
        curr = self.head
        while curr:
            print(curr.val, end = '->')
            curr = curr.nxt
        print(None)
    def __iter__(self):
        return self.Iterator(self)

class Stack:
    def __init__(self):
        self.stack = LinkedList()
    
    def push(self, val): 
        self.stack.add(val)
    def empty(self):
        if self.stack.head:
            return False
        return True
    def seek(self):
        if not self.empty():
            return self.stack.head.val
        return None
    def pop(self):
        if not self.empty(): 
            val = self.stack.head.val
            self.stack.rm_head()
            return val
        return None
    
