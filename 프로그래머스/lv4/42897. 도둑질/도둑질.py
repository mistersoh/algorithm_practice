def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)
    
    dp1[0] = money[0]
    dp1[1] = max(money[0],money[1])

    dp2[1] = money[1]
    
    for i in range(2, len(money)-1):
        
        dp1[i] = max(dp1[i-1], dp1[i - 2] + money[i])
    
    for j in range(1, len(money)):
        dp2[j] = max(dp2[j-1], dp2[j - 2] + money[j])
    
    return max(max(dp1),max(dp2))