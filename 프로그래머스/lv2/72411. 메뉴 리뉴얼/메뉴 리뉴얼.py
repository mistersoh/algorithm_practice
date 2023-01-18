from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    
    for c in course:
        
        combination = []
        
        for order in orders:
            combination += list(combinations(sorted(order),c))
        combination = Counter(combination)
        print("c=",c,combination)
        answer+=[''.join(k) for k, v in combination.items() if v == max(combination.values()) and v>1]

    return sorted(answer)