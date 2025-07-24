def solution(name):
    n = len(name)
    
    # 세로 조작 계산
    moves = []
    for c in name:
        moves.append(min(ord(c) - ord('A'), 26 - (ord(c) - ord('A'))))
    vertical_moves = sum(moves)
    
    # 가로 조작 계산
    horizontal_moves = n - 1
    
    # 연속된 A를 건너 뛸 수 있나
    for i in range(n):
        
        next_i = i + 1
        
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        
        horizontal_moves = min(horizontal_moves, i + n - next_i + min(i, n - next_i))
    
    return vertical_moves + horizontal_moves