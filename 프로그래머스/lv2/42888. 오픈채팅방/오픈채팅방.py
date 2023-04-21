from collections import defaultdict

def solution(record):
    answer = []
    uid_name_dict = defaultdict(str)
    
    for i in record:
        command = i.split()[0]
        
        if command != "Leave":
            uid, nickname = i.split()[1],i.split()[2]
            uid_name_dict[str(uid)] = nickname
            
            if command == "Enter":
                answer.append([uid,"님이 들어왔습니다."])
                
        if command == "Leave":
            uid = i.split()[1]
            answer.append([uid,"님이 나갔습니다."])
            
    for j in range(len(answer)):
        origin_uid = answer[j][0]
        answer[j][0] = uid_name_dict[origin_uid]
        answer[j] = ''.join(answer[j])
        
    return answer