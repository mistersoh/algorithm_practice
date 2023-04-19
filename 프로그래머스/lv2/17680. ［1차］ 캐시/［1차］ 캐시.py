def solution(cacheSize, cities):
    answer = 0
    mem =  []
    
    for c in cities:
        c = c.lower()
        if cacheSize:
            if c not in mem:
                if len(mem) == cacheSize:
                    mem.pop(0)
                mem.append(c)
                answer += 5
            
            else:
                mem.pop(mem.index(c))
                mem.append(c)
                answer += 1
        else:
            answer += 5
            
    
    return answer