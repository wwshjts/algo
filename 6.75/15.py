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
    def pr(self):
        print(self.__vector)
arr = Vector()    
for i in range(1, 12):
    arr.put(i)
    arr.pr()
for i in range(8):
    arr.pop()
    arr.pr()