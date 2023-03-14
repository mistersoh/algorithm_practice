def solution(n):

    ones_len = bin(n)[2:].count("1")
    
    while True:
        n += 1
        
        if bin(n)[2:].count("1") == ones_len:
            return n