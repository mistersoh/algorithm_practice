from collections import deque

def solution(maps):
    directions = ((1,0),(-1,0),(0,1),(0,-1))
    map_r, map_c = len(maps), len(maps[0])
    visited = set()
    path = 0
    que = deque([((0,0),path)])
    
    while que:
        loc,path = que.popleft()
        if loc == (map_r-1,map_c-1):
            return path + 1
        
        for d in directions:
            r1,c1 = loc[0]+d[0],loc[1]+d[1]
            curr_point = (r1,c1)
            # if (0 <= r1 < map_r and 0 <= c1 < map_c and maps[r1][c1] != 0 and curr_point not in visited):
            if 0 > r1 or r1 >= map_r or 0 > c1 or c1 >= map_c or maps[r1][c1] == 0 or curr_point in visited:
                continue
            else:
                visited.add(curr_point)
                que.append((curr_point,path+1))
            # else:
            #     continue
    return -1