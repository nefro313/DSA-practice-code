arr = [7,5,4,1,6]
n = len(arr)

for i in range(n):
    min_index = i
    print('{}.iteration'.format(i))
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]
