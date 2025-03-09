from collections import deque

def solution(board):
    answer = 0
    
    start = None
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] =="R":
                start = (i,j)
                break
                
        if start:
            break
    
    goal = None
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] =="G":
                goal = (i,j)
                break
                
        if goal:
            break
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    queue = deque([(start[0],start[1],0)])
    
    visited = set()
    visited.add(start)
    
    while queue:
        x,y,d = queue.popleft()
        
        if(x,y)==goal:
            return d
        
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx+dx < len(board) and 0 <= ny + dy < len(board[0]) and board[nx+dx][ny+dy] != 'D':
                nx += dx
                ny += dy
                
            if (nx,ny) not in visited:
                visited.add((nx,ny))
                queue.append((nx,ny,d+1))
                
    
    return -1