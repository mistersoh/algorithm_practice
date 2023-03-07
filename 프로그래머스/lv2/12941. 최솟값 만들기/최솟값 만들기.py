def solution(A,B):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i,j in zip(sorted(A),sorted(B)[::-1]):
        answer += i*j

    return answer