arr = [4,3,2,14,3,21]
largest = second_large = arr[0]
for num in arr:
    if num>largest:
        second_large = largest
        largest = num
    elif num > second_large and num != largest:
        second_large = num

print(second_large)