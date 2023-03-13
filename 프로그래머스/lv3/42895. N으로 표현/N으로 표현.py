def solution(N, number):
    answer = -1
    dp = [set([int(str(N)*i)]) for i in range(1,9)]
    
    for i in range(8):        
        for j in range(0,i):

            for x in dp[j]:
                for y in dp[i-j-1]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
                    if x != 0:
                        dp[i].add(y // x)
        if number in dp[i]:
            answer = i + 1
            break
                
    return answer