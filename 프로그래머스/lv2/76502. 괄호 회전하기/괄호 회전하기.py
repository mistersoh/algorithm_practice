def solution(s):
    answer = 0
    s_len = len(s)
    
    while s_len >= 1:
        stack = []
        correct = True
        for i in s:
            if i == "[" or i == "{" or i == "(":
                stack.append(i)
            
            elif stack and ((i == "]" and stack[-1] == "[") or (i == "}" and stack[-1] == "{") or (i == ")" and stack[-1] == "(")):
                stack.pop()
            else:
                correct = False
                break

        if not stack and correct:
            answer += 1
            
        next_s = s[1:] + s[:1]
        s = next_s
        s_len -= 1
        
    return answer