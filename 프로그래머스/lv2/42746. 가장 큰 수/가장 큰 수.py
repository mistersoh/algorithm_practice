def solution(numbers):
    answer = ''
    numbers.sort(reverse=True, key = lambda x : str(x)*4)
    
    if len(numbers) == numbers.count(0):
        return "0"
    
    answer=''.join(str(s) for s in numbers)
    
    return answer