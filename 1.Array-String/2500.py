

def deleteGreatestValue(grid) -> int:
    row_len = len(grid[0])
    res = 0
    max_ele = 0
    for j in range(row_len):
        for i in range(len(grid)):
            sorted_row = sorted(grid[i])
            max_ele = max(max_ele,sorted_row.pop())
            print(grid)
            print(max_ele)
        res+=max_ele
    print(grid)
    return res
            
        
        

grid = [[1,2,4],[3,3,1]]

# nn = grid[0].pop()
# print(grid)
print(deleteGreatestValue(grid))