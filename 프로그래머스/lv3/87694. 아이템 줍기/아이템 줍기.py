from collections import deque, defaultdict

def find_all_edeges(rectangles):

    edges = defaultdict(int)

    for rec in rectangles:
        minX,minY,maxX,maxY = min(rec[0],rec[2])*2, min(rec[1],rec[3])*2, max(rec[0],rec[2])*2, max(rec[1],rec[3])*2

        for x in range(minX, maxX+1):
            for y in range(minY,maxY+1):
                edges[(x,y)] += 1

    return edges

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    directions = ((1,0),(-1,0),(0,1),(0,-1))
    border_directions = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1))
    visited = set()
    que = deque([((characterX*2,characterY*2),answer)])
    
    area = find_all_edeges(rectangle)
    borders = []
    for k,v in list(area.items()):

        area_cnt = 0
        x = k[0]
        y = k[1]

        for d in border_directions:
            dx = d[0]
            dy = d[1]
            if (x+dx, y+dy) in area:
                area_cnt += 1

        if area_cnt <= 7:
            borders.append((x,y))
    

    borders_list = sorted(set(borders))

    # print(borders_list)

    while que:
        # print(que)
        loc,answer = que.popleft()
        x = loc[0]
        y = loc[1]
        visited.add((x,y))
        if x <= 100 and y <= 100 and x >= 0 and y >= 0:
            if (x,y) == (itemX*2,itemY*2):
                return answer//2

            for d in directions:
                x1, y1 = x + d[0], y + d[1]
                curr_point = (x1,y1)
                # if curr_point == (3,6) or curr_point == (2,6):
                #     print(curr_point)
                if curr_point not in visited and curr_point in borders_list:
                    # print(curr_point,answer)
                    que.append((curr_point, answer+1))
                else:
                # que.popleft()
                    continue


    return answer
