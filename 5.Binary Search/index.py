
def bst (arr, item, low, high):
    if low<=high:
        mid = low + (high - low)//2
        if item == arr[mid]:
            return True
        elif item < arr[mid]:
            return bst(arr,item,low,mid - 1)
        else:   
            return bst(arr,item,mid+1,high) 
    else:
        return False
        
arr = [7,5,4,1,6]
arr.sort()
ans = bst(arr, 99, 0, len(arr) - 1)
print(ans)