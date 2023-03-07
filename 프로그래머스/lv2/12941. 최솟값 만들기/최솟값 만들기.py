def solution(A,B):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])