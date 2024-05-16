def find_max_area(matrix):
    max_area = 0
    # create an array with the given row and column
    visited = [[False] * len(matrix[i]) for i in range(len(matrix))]
    stack = []
    direction = [(0,1),(0,-1),(1,0),(-1,0)]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(not visited[i][j]):
                area = 0
                stack.append((i,j))
                visited[i][j] = True

                while stack:
                    x,y = stack.pop()
                    area += 1

                    for dx,dy in direction:
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[i]) and not visited[nx][ny] and matrix[nx][ny] == matrix[x][y]:
                            stack.append((nx,ny))
                            visited[nx][ny] = True
                max_area = max(max_area, area)
    return max_area

row,col = map(int,input().split(' '))
# create a tuple of lists with the given row and column
matrix = [0] * row
# read the matrix values
for i in range(row):
    matrix[i] = tuple(map(int, input().split(' ')))
 
print(find_max_area(matrix))
