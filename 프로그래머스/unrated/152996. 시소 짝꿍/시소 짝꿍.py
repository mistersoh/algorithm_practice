from collections import defaultdict, Counter

def solution(weights):
    
    answer = 0
    
    weights_counter = Counter(weights)
    
    for w in weights_counter:
        if weights_counter[w] >= 2:
            answer += weights_counter[w] * (weights_counter[w] - 1) // 2
            
    weights = set(weights)
    
    for weight in weights:
        weight_2_3 = weight*2/3
        weight_2_4 = weight*2/4
        weight_3_4 = weight*3/4
        
        if weight_2_3 in weights:
            answer += weights_counter[weight_2_3] * weights_counter[weight]
        
        if weight_2_4 in weights:
            answer += weights_counter[weight_2_4] * weights_counter[weight]
        
        if weight_3_4 in weights:
            answer += weights_counter[weight_3_4] * weights_counter[weight]
    return answer