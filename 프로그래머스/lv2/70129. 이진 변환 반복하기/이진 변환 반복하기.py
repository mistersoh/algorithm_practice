def solution(s):
    answer = []
    zero_nums = 0
    bin_change = 0
    while s != "1":
        zero_nums += s.count("0")
        s = s.replace("0","")
        s = str(format(len(s), 'b'))
        bin_change += 1
    answer.append(bin_change)
    answer.append(zero_nums)
    return answer