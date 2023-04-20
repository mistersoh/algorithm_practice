from collections import Counter

def solution(str1, str2):
    str1_low = str1.lower()
    str2_low = str2.lower()
    
    str1_comb = []
    str2_comb = []
    
    for i in range(len(str1_low)-1):
        current_1 = i
        next_1 = i+1

        if str1_low[current_1].isalpha() and str1_low[next_1].isalpha():
            str1_comb.append(str1_low[current_1] + str1_low[next_1])

    for j in range(len(str2_low)-1):
        current_2 = j
        next_2 = j+1

        if str2_low[current_2].isalpha() and str2_low[next_2].isalpha():
            str2_comb.append(str2_low[current_2] + str2_low[next_2])
            
    str1_count = Counter(str1_comb)
    str2_count = Counter(str2_comb)
    
    common_str = len(list((str1_count & str2_count).elements()))
    all_str = len(list((str1_count | str2_count).elements()))
    
    if common_str + all_str == 0:
        return 65536
    else:
        return int((common_str/all_str) * 65536)
    