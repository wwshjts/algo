
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

class Vector:
    def __init__(self, size = 10):
        self.__vector = [0] * size
        self.__head = 0
        self.__size = size
        
    def __alloc(self):
        tmp = [0] * self.__size * 2
        for i in range(self.__size):
            tmp[i] = self.__vector[i] 
        self.__vector = tmp
        self.__size *= 2
    def __shrink(self):
        tmp = [0] * (self.__size // 2)
        for i in range(self.__size//4 + 1):
            tmp[i] = self.__vector[i] 
        self.__vector = tmp 
        self.__size = self.__size // 2
    def put(self, var):
        if self.__head == self.__size:
            self.__alloc()
        self.__vector[self.__head] = var
        self.__head += 1
    def pop(self):
        if self.__head == 0:
            return None
        if self.__head <= (self.__size // 4):
            self.__shrink()
        self.__head -= 1
        return(self.__vector[self.__head]) 
    @property 
    def pr(self):
        print(self.__vector)
    @property
    def len(self):
        return self.__head
    def __getitem__(self, i):
        return self.__vector[i]
    def __setitem__(self, i, val):
        self.__vector[i] = val


class BinaryHeap:
    def __init__(self, size = 1):
        self.a = Vector(size = size)
    #return's list of existing leaves indexes
    def leaves(self, i):
        res = []
        if 2 * i + 1 < self.a.len:
            res.append(2 * i + 1)
        if 2 * i + 2 < self.a.len:
            res.append(2 * i + 2)
        return res
    #returns index of node's parent
    def parent(self, i):
        if i > 0:
            return (i - 1) // 2
        return 0
    def heapify_down(self):
        leaves = self.leaves(0)
        curr = 0
        while any([self.a[leaf] >= self.a[curr] for leaf in leaves]):
            if len(leaves) == 1:
                self.a[curr], self.a[leaves[0]] = self.a[leaves[0]], self.a[curr]
                curr = leaves[0]
            else:
                max_leaf = leaves[0] if self.a[leaves[0]] >= self.a[leaves[1]] else leaves[1]
                self.a[curr], self.a[max_leaf] = self.a[max_leaf], self.a[curr] 
                curr = max_leaf
            leaves = self.leaves(curr)
    def heapify_up(self):
        curr = self.a.len - 1
        par = self.parent(curr)
        while (curr > 0) or (self.a[curr] > self.a[par]):
            self.a[curr], self.a[par] = self.a[par], self.a[curr]
            curr = par
            par = self.parent(curr)
    def insert(self, val):
        self.a.put(val)
        self.heapify_up()
    def print(self):
        self.a.pr
    def extract_max(self):
        self.a[0], self.a[self.a.len - 1] = self.a[self.a.len - 1], self.a[0]
        self.a.pop()
        self.heapify_down()
    @property
    def max(self):
        if self.a.len > 0:
            return self.a[0]
        return None

class PriorityQue:
    class Pair:
        def __init__(self, pr, value):
            self.pair = (pr, value)
        def __gt__(self, op):
            op1 = self.pair
            op2 = op.pair
            if op1[0] > op2[0]:
                return True
            return False
        def __ge__(self, op):
            op1 = self.pair
            op2 = op.pair
            if op1[0] >= op2[0]:
                return True
            return False
    def __init__(self):
        self.que = BinaryHeap()
    def insert(self,pr, value):
        self.que.insert(self.Pair(pr, value))
    def peek_max(self):
        return self.que.max
    def print(self):
        for i in range(self.que.a.len):
            print(self.que.a[i].pair)