def solution(s):
    answer = []
    spliter = ["{","}",","]
    
    s1 = s[2:-2].split("},{")
    s1 = sorted(s1, key=len)
    for i in s1:
        for j in i.split(","):
            if int(j) not in answer:
                answer.append(int(j))
                
    return answer
    
    # for i in set(s):
    #     if i != '{' and i != "}" and i != ",":
    #         answer.append(int(i))
    
    # return answer