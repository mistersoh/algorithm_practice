import math

def solution(s):
    answer = ''
    max_n = -math.inf
    min_n = math.inf
    for i in s.split():
        max_n = max(max_n, int(i))
        min_n = min(min_n, int(i))
        
    answer = str(min_n) + ' ' + str(max_n)
    return answer