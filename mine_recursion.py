def dfs(value, i, j, matrix, visited):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[i]) or (i, j) in visited or matrix[i][j] != value:
        return 0
    visited.add((i, j))
    area = 1
    area += dfs(value, i - 1, j, matrix, visited)
    area += dfs(value, i + 1, j, matrix, visited)
    area += dfs(value, i, j - 1, matrix, visited)
    area += dfs(value, i, j + 1, matrix, visited)
    
    return area

def find_max_area(matrix):
    max_area = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            area = dfs(matrix[i][j], i, j, matrix, visited=set())
            max_area = max(max_area, area)
    return max_area

row,col = map(int,input().split(' '))
# create a tuple of lists with the given row and column
matrix = [0] * row
# read the matrix values
for i in range(row):
    matrix[i] = tuple(map(int, input().split(' ')))
 
print(find_max_area(matrix))
