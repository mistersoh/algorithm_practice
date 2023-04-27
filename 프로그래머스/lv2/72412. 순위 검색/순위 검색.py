from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    
    for i in info:
        info_split = i.split()
        score_info = info_split[-1]
        rest_info = info_split[:-1]
        
        for j in range(5):
            for c in combinations(rest_info, j):
                tmp = ''.join(c)
                info_dict[tmp].append(int(score_info))
    for info in info_dict:
        info_dict[info].sort()
    
    for q in query:
        query_split = q.split()
        score_query = query_split[-1]
        rest_query = ''.join(list(map(lambda x: x.replace('and','').replace('-','') ,query_split[:-1])))
        
        if rest_query in info_dict:
            list_scores = info_dict[rest_query]
        
            if list_scores and score_query.isdigit():
                answer.append(len(list_scores)-bisect_left(list_scores, int(score_query)))
        else:
            answer.append(0)
    return answer