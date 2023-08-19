from itertools import permutations


def join_tup(tup):
    res = tup[0]
    for idx in tup[1:]:
        res = res * 10 + idx
    return res

def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    combination_list = []
    
    num_digits = len(numbers)
    
    numbers = [int(x) for x in str(numbers)]
    for i in range(1,num_digits+1):
        
        list_of_nums = list(permutations(numbers,i))
        
        
        for j in list_of_nums:
            
            joint_j = join_tup(j)
            
            combination_list.append(joint_j)
            
    combination_list = set(combination_list)

    for k in combination_list:
        
        if is_prime(k) and k > 1:
            answer += 1
        
    
    return answer