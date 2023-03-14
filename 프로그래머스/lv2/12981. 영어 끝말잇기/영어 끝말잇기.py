from collections import defaultdict

def solution(n, words):
    word_count = defaultdict(int)
    
    word_count[words[0]] += 1
    count = 0

    for i in range(1,len(words)):
        count += 1
        word = words[i]
        prev_word = words[i-1]
        word_count[word] += 1
        
        if word_count[word] > 1 or word[0] != prev_word[-1]:

            return([i%n+1,i//n+1])
        
    return [0,0]