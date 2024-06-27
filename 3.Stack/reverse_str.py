
s_tr = 'robin'
Stack=list(s_tr)
new_str = ''
for i in range(len(s_tr)):
    new_str += Stack.pop()
print(new_str)