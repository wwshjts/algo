from data_struct import *
precedence = {None : 3, '!' : 0, '~': 0, '^' : 0, '*' : 1, '/' : 1, '%' : 1, 
              '+' : 2 , '-' : 2, }
right_to_left = {'!', '~'}
stack = Stack()
inp = input('> ').split(' ')
result = ''
for item in inp:
    if item.isnumeric():
        result += item
    else:
        n_rtl = (item not in right_to_left) and (precedence[stack.seek()] == precedence[item])
        while ( (precedence[stack.seek()] < precedence[item]) or n_rtl):
            result += stack.pop()
            n_rtl = (item not in right_to_left) and (precedence[stack.seek()] == precedence[item])
        stack.push(item)
while not stack.empty():
    result += stack.pop()
print(result)
    

        
    