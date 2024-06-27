Stack = []
Stack.append(1) # pushing adding element in the stack 
Stack.append(3) # pushing adding element in the stack 
Stack.append(2) # pushing adding element in the stack 
Stack.append(15) # pushing adding element in the stack 
Stack.append(10) # pushing adding element in the stack 
print(Stack)
pop = Stack.pop()
print(pop)
peek = Stack[-1]
print(peek)
is_empty =  True if len(Stack) == 0 else False
print(is_empty)

