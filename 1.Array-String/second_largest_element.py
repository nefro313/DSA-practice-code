arr = [4,3,2,14,3,21]

l = arr[0]

# Find the second element in the array
sl = arr[0]
for i in range(1, len(arr)):
    if arr[i] > l:
        sl = l
        l = arr[i]
    elif arr[i] > sl and arr[i] != l:
        sl = arr[i] 
print(sl)       

# # Find the largest element in the array
# for i in range(1,len(arr)):
#     if arr[i] > l:
#         l = arr[i]
# print(l)