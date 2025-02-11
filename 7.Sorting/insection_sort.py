arr = [7,5,4,1,6]
n = len(arr)

for i in range(1,n):
    key = arr[i]
    pos = i
    while arr[pos-1]> key and pos>0:
        arr[pos] = arr[pos-1]
        pos-=1
    arr[pos] = key
print(arr)