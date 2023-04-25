def solution(land):
    answer = 0
    
    dp = land
    
    for i in range(1,len(land)):
        
        for j in range(4):
            
            dp[i][j] += max(dp[i-1][:j] + dp[i-1][j+1:])
    answer = max(dp[len(dp)-1])
    return answer