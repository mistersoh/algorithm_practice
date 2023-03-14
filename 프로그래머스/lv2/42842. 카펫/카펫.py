def solution(brown, yellow):
    answer = []
    
    for h in range(1,int(yellow**0.5)+1):
        
        if yellow%h == 0:
            w = yellow//h
            if (h <= w) and (w+2) * (h+2) == brown+yellow:
                answer.append(w+2)
                answer.append(h+2)
    
    return answer