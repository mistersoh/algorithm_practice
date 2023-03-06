def solution(s):
    answer = ''
    print(s)
    Upper = False
    for n,char in enumerate(s):
        if char == ' ':
            Upper = True
            answer += char
        elif Upper or n==0:
            
            answer += char.upper()
            Upper = False
        else:
            answer += char.lower()
    return answer