def solution(grid):
    dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    
    rows, columns = len(grid), len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(columns)] for _ in range(rows)]
    ans = []
    
    for i in range(rows):
        for j in range(columns):
            for k in range(4):
                if not visited[i][j][k]:
                    dx, dy, dd = i, j, k
                    count = 0
                    
                    while not visited[dx][dy][dd]:
                        visited[dx][dy][dd] = True
                        count += 1
                        
                        nx, ny = dir[dd]
                        dx, dy = (dx + nx) % rows, (dy + ny) % columns
                        
                        if grid[dx][dy] == 'L':
                            dd = (dd-1) % 4
                        elif grid[dx][dy] == 'R':
                            dd = (dd+1) % 4
                            
                    ans.append(count)
                        
    return sorted(ans)