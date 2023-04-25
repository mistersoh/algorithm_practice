from itertools import permutations

def solution(k, dungeons):
    len_dun = len(dungeons)
    max_dun = 0
    
    for permute in permutations(range(len_dun)):
        
        target_k = k
        
        for dun_num, dun_loc in enumerate(permute):
            
            if target_k < dungeons[dun_loc][0]:
                max_dun = max(max_dun,dun_num)
                break
            
            target_k -= dungeons[dun_loc][1]
            
        else:
            return len_dun
            
    return max_dun
                