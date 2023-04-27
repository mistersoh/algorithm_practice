def solution(n):
    answer = []
    triangle = [[0 for _ in range(1,i + 1)] for i in range(1,n+1)]
    depth, pointer = -1, 0
    
    num = 1
    
    for side in range(n):
        for _ in range(side,n):
            
            if side % 3 == 0:
                depth += 1
                
            elif side % 3 == 1:
                pointer += 1
                
            else:
                depth -= 1
                pointer -= 1
            
            triangle[depth][pointer] = num
            num += 1
    for sub_list in triangle:
        answer.extend(sub_list)
    
    return answer