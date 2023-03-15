from collections import Counter

def solution(people, limit):
    answer = 0
    sorted_people = sorted(people)
    # print(sorted_people)
    pointer1 = 0
    pointer2 = len(sorted_people) -1
    while pointer1 <= pointer2:
        
        if sorted_people[pointer1] + sorted_people[pointer2] <= limit:
            answer += 1
            pointer1 += 1
            pointer2 -= 1
        else:
            answer += 1
            pointer2 -= 1
            
    return answer
            