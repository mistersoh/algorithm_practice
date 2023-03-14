def solution(s):
    stack = []
    
    if len(s) % 2 == 1:
        return 0
    
    for i in s:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if stack:
        return 0
    return 1