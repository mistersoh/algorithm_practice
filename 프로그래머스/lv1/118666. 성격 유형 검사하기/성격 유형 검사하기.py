def solution(survey, choices):
    answer = ["R","C","J","A"]

    points_dict = {
        1:3,
        2:2,
        3:1,
        4:0,
        5:1,
        6:2,
        7:3
    }

    character_dict = {
        "R":0,
        "C":0,
        "J":0,
        "A":0,
        "T":0,
        "F":0,
        "M":0,
        "N":0
    }

    positives = [1,2,3,4]

    for ans in zip(survey,choices):
        char,point = ans[0][0],ans[1]

        if point in positives:
            point = points_dict[point]
        else:
            point = -points_dict[point]

        character_dict[char] += point

        if character_dict["R"] < character_dict["T"]:
            answer[0] = "T"
        else:
            answer[0] = "R"

        if character_dict["C"] < character_dict["F"]:
            answer[1] = "F"
        else:
            answer[1] = "C"

        if character_dict["J"] < character_dict["M"]:
            answer[2] = "M"
        else:
            answer[2] = "J"

        if character_dict["A"] < character_dict["N"]:
            answer[3] = "N"
        else:
            answer[3] = "A"


    return ''.join(answer)