"""Questions1:"""
"""Given an array of integers num and an integer target, return
indices of the two numbers such that they add up to target."""
"""input:Array,Integer """
"""output:Array of indices"""
arr = [3,2,2,9,6,4]
target = 8
#Brute-Force Approach
def two_sum(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!= j and arr[i]+arr[j] == target:
                return[i,j] 
ans = two_sum(arr,target)
print(ans)

#Optimize Approach

def o_two_sum(arr,target):
    d = {}
    for i,val in enumerate(arr):
        t = target - val
        if t in d:
            return[d[t],i]
        else:
            d[val] = i
ans = o_two_sum(arr,target)
print(ans)
  
