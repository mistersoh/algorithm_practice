def solution(arr):
    # answer = 0
    arr = sorted(arr)
    answer = arr[0]
    
    for i in range(1, len(arr)):
        for j in range(arr[i], answer * arr[i] + 1, arr[i]):
            if j % answer == 0 and j % arr[i] == 0:
                answer = j
                break
                
    return answer