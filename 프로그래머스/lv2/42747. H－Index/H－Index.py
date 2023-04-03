def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h = 0
    max_h = 0
    for i in citations:
        h += 1
        if i >= h:
            answer = h
        else:
            break
    
    return answer