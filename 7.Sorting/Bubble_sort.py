arr = [7,5,4,1,6]
n = len(arr)

for i in range(n):
    swapped = False 
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swapped = True
    if swapped is not True:
        break
        
print(arr)